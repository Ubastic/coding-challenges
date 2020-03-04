Object.prototype.hierarchy = function () {
    return [...chain(this, "prototype")].map(obj => obj.name || obj.__proto__.constructor.name);
};

Object.prototype.copyContext = function () {
    let newContext = Object.assign({}, this);
    Object.keys(this).forEach(key => newContext[key] = [...newContext[key]]);

    return newContext;
};

String.prototype.resolve = function () {
    if (!!global[this])
        return global[this];

    return eval(this[0].toUpperCase() + this.slice(1))
};

String.prototype.types = function () {
    return this.split(",").map(s => s.trim());
};

Array.prototype.remove = function (value) {
    return this.filter((obj, i) => i !== this.indexOf(value));
};

Array.prototype.same = function (other) {
    return JSON.stringify(this) === JSON.stringify(other);
};

Array.prototype.filterTypes = function (args) {
    return this.filter(fn => fn.is_types_match(...args))
};

Array.prototype.apply = function (args) {
    return this.forEach(fn => fn(...args));
};

function callNextMethod(methodInfo, ...args) {
    let newMethod = methodInfo.next();

    try {
        return newMethod(...args);
    } catch (e) {
        let name = !!methodInfo.context.primary.length ? "primary" : "around";
        throw "No next method found for describe in " + name;
    }
}

function* chain(node, attr = "__proto__") {
    while (!!node && node !== Object.prototype) {
        yield node;
        node = node[attr];
    }
}

let type_match = (t, a) => (
    [...chain(a)].some(arg => arg instanceof Object && arg.constructor.name === t)
    || (a === null && t === 'null')
    || (typeof a === t)
    || (t === '*')
);

let compare_type = (t1, t2) => {
    if (t1 === t2)
        return 0;
    if (t1 === "*")
        return 1;
    if (t2 === "*")
        return -1;

    let obj1 = t1.resolve(), obj2 = t2.resolve();

    if (obj1.hierarchy().includes(obj2.name))
        return -1;
    else if (obj2.hierarchy().includes(obj1.name))
        return 1;

    return 0;
};

let compare_types = (func1, func2) => {
    if (func1.types.length > func2.types.length)
        return 1;
    else if (func1.types.length < func2.types.length)
        return -1;

    for (let i = 0; i < func1.types.length; i++) {
        let t1 = func1.types[i], t2 = func2.types[i];

        let specific = compare_type(t1, t2);
        if (specific === 0)
            continue;

        return specific;
    }

    return 0;
};

class Callable extends Function {
    constructor(fn, types, combination, context = null, skip = 0, force = undefined) {
        super('return arguments.callee._call.apply(arguments.callee, arguments)');
        this.fn = fn;
        this.types = types;
        this.combination = combination;
        this.context = context;
        this.skip = skip;
        this.force = force;
    }

    _call(...args) {
        if (!!this.force)
            return this.force(...args);

        let [, fn] = func(this.context, this.skip, ...args);
        return fn(...args);
    }

    next() {
        return new Callable(this.fn, this.types, this.combination, this.context, this.skip + 1);
    }

    is_types_match(...args) {
        return (
            args.length === this.types.length
            && args.every((arg, i) => type_match(this.types[i], arg))
        )
    }
}

function func(context, skip = 0, ...args) {
    let original_skip = skip;

    let around = context.around.filterTypes(args).sort(compare_types);

    if (around.length - skip > 0) {
        let [fn, ..._] = around.slice(skip);

        let f = fn.next();
        f.skip = original_skip;

        return [fn, (...a) => f.fn(...a)];
    }

    skip -= around.length;
    let fns = context.primary.filterTypes(args).sort(compare_types).slice(skip);

    if (fns.length === 0)
        throw Error();

    let before = [...context.before.filterTypes(args).map(f => f.fn)];
    let after = [...context.after.filterTypes(args).reverse().map(f => f.fn)];

    let [fn,] = fns;
    let f = fn.next();
    f.skip = original_skip;

    return [fn, (...a) => {
        if (!skip)
            before.forEach(f => f(...a));

        let res = f.fn(...a);

        if (!skip)
            after.forEach(f => f(...a));

        return res;
    }];
}


function defgeneric(name) {
    let generic = function (...args) {
        return generic.findMethod(...args)(...args);
    };

    generic.functions = {
        primary: [],
        before: [],
        after: [],
        around: [],
    };
    generic.cache = new Map();

    generic.addFunction = function (combination, fn) {
        generic.functions[combination] = [...generic.functions[combination], fn].sort(compare_types);
        generic.cache.clear();
    };

    generic.removeFunction = function (fn, ...key) {
        let copy = Object.assign({}, generic.functions);
        let keys = key.length === 0 ? Object.keys(generic.functions) : [...key];
        keys.forEach(key => copy[key] = copy[key].remove(fn));
        generic.cache.clear();

        return copy;
    };

    generic.defmethod = (discriminator, fn, combination = 'primary') => {
        let types = discriminator.types();

        generic.functions[combination] = generic.functions[combination].filter(f => !f.types.same(types));

        generic.addFunction(combination, new Callable(fn, types, combination, generic.functions));
        generic.cache.clear();

        return generic;
    };

    generic.removeMethod = (discriminator, combination = 'primary') => {
        let types = discriminator.types();
        let [fn,] = generic.functions[combination].filter(fn => fn.types.same(types));

        generic.functions = generic.removeFunction(fn, combination);
        generic.cache.clear();

        return generic;
    };

    generic.findMethod = (...args) => {
        let fn, force;

        try {
            [fn, force] = func(generic.functions, 0, ...args);
        } catch (e) {
            throw "No method found for append with args: " + args.map(s => typeof s).join();
        }

        let key = fn.fn;

        if (generic.cache.has(key)) {
            return generic.cache.get(key);
        }

        let obj = new Callable(fn.fn, fn.types, fn.combination, generic.functions.copyContext(), 0, force);
        generic.cache.set(key, obj);

        return obj;
    };

    return generic;
}