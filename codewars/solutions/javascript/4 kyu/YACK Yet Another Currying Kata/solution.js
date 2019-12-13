function yack(func, ...initArgs) {
    let create = f => (...args) => {
        let carried = (...a) => f(...a);
        carried.args = [...(f.args || []), ...args];
        carried.len = f.len || f.length;
        carried.wraps = f;
        return carried.args.length >= carried.len ? carried(...carried.args) : create(carried);
    };

    return create(func.wraps || func)(...initArgs);
}