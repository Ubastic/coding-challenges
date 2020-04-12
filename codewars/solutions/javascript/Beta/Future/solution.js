class Future {
    constructor() {
        this.args = undefined;
        this.callbacks = [];
    }

    fulfill(...args) {
        if (this.args)
            throw Error();

        this.args = args;
        this.check();
    }

    when(callback) {
        this.callbacks.push(callback);
        this.check();
    }

    isResolved() {
        return this.args && this.callbacks.length;
    }

    check() {
        if (this.isResolved())
            this.callbacks.forEach(c => c(...this.args));
    }
}

class Join {
    constructor() {
        this.futures = [];
    }

    add(future) {
        this.futures.push(future);
    }

    when(callback) {
        new Promise((resolve) => {
            let resolved = 0;
            this.futures.forEach(c => c.when(() => {
                if (++resolved === this.futures.length)
                    resolve();
            }));
        }).then(() => callback(this.futures.map(f => f.args[0]), this.futures.map(f => f.args[1])));
    }
}