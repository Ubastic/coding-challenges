class Future {
    constructor() {
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

    check() {
        if (this.args && this.callbacks.length)
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
        let resolved = 0;
        this.futures.forEach(c => c.when(() => {
            if (++resolved === this.futures.length)
                callback(this.futures.map(f => f.args[0]), this.futures.map(f => f.args[1]))
        }));
    }
}