function getArgs(func) {
    return (func + '')
        .replace(/[/][/].*$/mg, '')
        .replace(/\s+/g, '')
        .replace(/[/][*][^/*]*[*][/]/g, '')
        .split('){', 1)[0].replace(/^[^(]*[(]/, '')
        .replace(/=[^,]+/g, '')
        .split(',').filter(Boolean);
}

function yack(func, ...initArgs) {
    let create = f => (...args) => {
        function carried(...a) {
            return f(...a);
        }

        Object.assign(carried, {
            args: [...(f.args || []), ...args],
            len: f.len || getArgs(f).length,
            wraps: f
        });
        return carried.args.length >= carried.len ? carried(...carried.args) : create(carried);
    };

    return create(func.wraps || func)(...initArgs);
}