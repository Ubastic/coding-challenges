let ensure = condition => {
    if (!condition) throw Error();
};

let literal = (...values) => tokens => {
    ensure(values.some(v => tokens[0].toLowerCase() === v.toLowerCase()));
    return [tokens[0], tokens.slice(1)];
};


let or = (...handlers) => tokens => {
    for (let h of handlers)
        try {return h(tokens);} catch (e) {}
    throw Error();
};


let and = (...handlers) => tokens => {
    let results = [], result;
    for (let h of handlers) {
        [result, tokens] = h(tokens);
        results.push(result);
    }
    return [results, tokens];
};

let _null = (tokens) => {
    ensure(tokens[0] === "null");
    return [null, tokens.slice(1)];
};

let _true = (tokens) => {
    ensure(tokens[0] === "true");
    return [true, tokens.slice(1)];
};

let _false = (tokens) => {
    ensure(tokens[0] === "false");
    return [false, tokens.slice(1)];
};

let _number = (tokens) => {
    ensure(tokens[0].match(/^((0|-?[1-9]\d*)(\.\d+)?)$/g));
    return [parseFloat(tokens[0]), tokens.slice(1)];
};

let _string = (tokens) => {
    ensure(tokens[0].match(/"[^"]*?"/g));
    return [tokens[0].slice(1, -1), tokens.slice(1)];
};

let _array = (tokens, val, strict = false, values = []) => {
    [, tokens] = literal("[")(tokens);

    while (true) {
        try {
            [val, tokens] = _value(tokens);
            values.push(val);

            if (tokens[0] !== ",")
                break;

            strict = true;
            [, tokens] = literal(",")(tokens);
        } catch (e) {
            if (strict) throw e;
            break;
        }
    }

    [, tokens] = literal("]")(tokens);
    return [values, tokens];
};

let _pair = (tokens, key, value, pairs = []) => {
    [[key, , value], tokens] = and(_string, literal(":"), _value)(tokens);
    pairs.push([key, value]);

    if (tokens[0] === ",") {
        let others;
        [others, tokens] = _pair(tokens.slice(1));
        pairs.push(...others);
    }

    return [pairs, tokens];
};

let _object = (tokens, pairs = null) => {
    [, tokens] = literal("{")(tokens);

    if (tokens[0] === "}")
        return [{}, tokens.slice(1)];

    [[pairs,], tokens] = and(_pair, literal("}"))(tokens);
    let obj = pairs.reduce((acc, pair) => (acc[pair[0]] = pair[1], acc), {});

    return [obj, tokens];
};


let _value = (tokens) => or(_string, _number, _object, _array, _false, _true, _null)(tokens);

let parse = str => {
    ensure(str.match(/^((true|false|null|"[^"]*?"|-?\d+(?:\.\d+)?|[\[\]{}:,])|\s)*$/g));
    let [res, tokens] = _value(str.match(/true|false|null|"[^"]*?"|-?\d+(?:\.\d+)?|[\[\]{}:,]/g));
    ensure(!tokens.length);

    return res;
};