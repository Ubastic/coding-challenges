let valid_name = name => /[a-zA-Z0-9_]+/.test(name);
let valid_const = token => /(\d+(\.\d+)?)|(['"](.*?)['"])/.test(token);

let fetch_one = tokens => {
    let [res, ...others] = tokens;
    return [res, others];
};

let ensure = condition => {
    if (!condition) throw Error();
};

let literal = (...values) => tokens => {
    ensure(values.some(v => tokens[0].toLowerCase() === v.toLowerCase()));
    return fetch_one(tokens);
};

let name = () => tokens => (ensure(valid_name(tokens[0])), fetch_one(tokens));
let variable = () => tokens => (ensure(valid_name(tokens[0]) || valid_const(tokens[0])), fetch_one(tokens));

let optional = (handler, defaultValue = []) => tokens => {
    try {
        return handler(tokens);
    } catch (e) {
        return [defaultValue, tokens];
    }
};

let multiple = (...handlers) => tokens => {
    let handler = and(...handlers);

    let results = [], result;
    while (true) {
        try {
            [result, tokens] = handler(tokens);
            results.push(result);
        } catch (e) {
            ensure(results.length > 0);
            return [results, tokens];
        }
    }
};

let and = (...handlers) => tokens => {
    let results = [], result;
    for (let h of handlers) {
        [result, tokens] = h(tokens);
        results.push(result);
    }
    return [results, tokens];
};

let parser = (tokens, ...handlers) => and(...handlers)(tokens);

Array.prototype.to = function (converter) {
    let [attrs, tokens] = this;
    return [converter(...attrs), tokens];
};

let sql_query = tokens => {
    let [q, others] = parser(tokens, select, from, optional(join), optional(where, null))
        .to((s, f, j, w) => ({select: s, from: f, joins: j, where: w}));
    ensure(others.length === 0);
    return q;
};

let select = tokens => parser(
    tokens, literal("select"), column_id, optional(multiple(literal(","), column_id))
).to((_, column, columns) => ({columns: [column, ...columns.map(v => v[1])]}));

let from = tokens => parser(tokens, literal("from"), name()).to((_, n) => ({table: n}));

let join = tokens => parser(
    tokens, literal("join"), name(), literal("on"), value_test, optional(multiple(join)),
).to((_, n, __, test, joins) => [{table: n, test: test}, ...(!!joins.length ? joins[0][0] : [])]);

let where = tokens => parser(tokens, literal("where"), value_test).to((_, test) => ({test: test}));

let column_id = tokens => {
    let table_name, column_name, name;
    [name, ...tokens] = tokens;
    [table_name, column_name] = name.split(".");
    ensure([table_name, column_name].map(valid_name));
    return [`${table_name}.${column_name}`, tokens];
};

let value_test = tokens => parser(
    tokens, variable(), literal("=", ">", "<", "<=", ">=", "<>"), variable(),
).to((left, op, right) => ({left: left, op: op, right: right}));

let COMPARISON = {
    "=": (a, b) => a === b,
    "<>": (a, b) => a !== b,
    ">": (a, b) => a > b,
    "<": (a, b) => a < b,
    ">=": (a, b) => a >= b,
    "<=": (a, b) => a <= b,
};

let convert_table = (name, table) => (
    table.map(row => Object.entries(row).reduce((acc, v) => (acc[`${name}.${v[0]}`] = v[1], acc), {}))
);

let convert_param = (row, param) => {
    let n = parseFloat(param);
    if (!Number.isNaN(n))
        return n;

    return param in row ? row[param] : param.slice(1, param.length - 1).replace("''", "'");
};

let apply_test = (row, test) => COMPARISON[test.op](convert_param(row, test.left), convert_param(row, test.right));

class SQLEngine {
    constructor(database) {
        this.database = Object.entries(database)
            .map(v => [v[0], convert_table(...v)])
            .reduce((acc, v) => (acc[v[0]] = v[1], acc), {})
    }

    execute(query) {
        let q = sql_query(query.match(/(['"](.*)['"])|,|([^,'\s]*)/g).filter(Boolean));

        let table = this.database[q.from.table];

        if (!!q.joins)
            for (let join of q.joins)
                table = table
                    .map(row => this.database[join.table].map(r => ({...row, ...r})).filter(r => apply_test(r, join.test)))
                    .reduce((acc, r) => (acc.push(...r), acc), []);

        if (!!q.where)
            table = table.filter(row => apply_test(row, q.where.test));

        if (!!q.select)
            table = table.map(row => q.select.columns.reduce((acc, column) => (acc[column] = row[column], acc), {}));

        return table;
    }
}
