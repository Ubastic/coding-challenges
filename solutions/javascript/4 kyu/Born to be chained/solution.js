function chain(fns, prev, fn, args) {
    let c = {prev: prev, state: fn !== undefined ? {'fn': fn, 'args': args} : null};
    c['execute'] = function () {
        let baseArgs = c.prev.prev !== undefined ? [c.prev.execute()] : [];
        return this.state === null ? [] : this.state['fn'](...baseArgs, ...this.state.args);
    };
    Object.entries(fns).forEach(value => c[value[0]] = (...args) => chain(fns, c, value[1], args));
    return c;
}