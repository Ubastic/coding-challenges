function Event() {
    let hnlds = [];
    this.subscribe = function (...args) {
        hnlds.push(...args.filter(h => typeof h === 'function'));
    };
    this.unsubscribe = function (...args) {
        args.filter(h => typeof h === 'function' && hnlds.includes(h))
            .forEach(h => hnlds.splice(hnlds.lastIndexOf(h), 1));
    };
    this.emit = function (...args) {
        [...hnlds].forEach(h => h.apply(this, args));
    };
}