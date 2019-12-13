function getArgs(func) {
    return (func + '')
        .replace(/[/][/].*$/mg, '')
        .replace(/\s+/g, '')
        .replace(/[/][*][^/*]*[*][/]/g, '')
        .split('){', 1)[0].replace(/^[^(]*[(]/, '')
        .replace(/=[^,]+/g, '')
        .split(',').filter(Boolean);
}

function defaultArguments(func, params) {
    let funcArgs = func.__args__ || getArgs(func);
    let wrapped = (...args) => func(...funcArgs.map((name, i) =>
        i < args.length ? args[i] : (args[i] === undefined ? params[funcArgs[i]] : args[i])
    ));

    wrapped.__args__ = funcArgs;
    return wrapped;
}