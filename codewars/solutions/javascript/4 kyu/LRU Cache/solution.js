function LRUCache(capacity, init = {}) {
    let store = {};
    let order = [];

    Object.defineProperty(this, "capacity", {
        get: () => capacity,
        set: (value) => {
            capacity = value;
            let diff = this.size - value;

            if (diff > 0)
                order.splice(0, diff).forEach(key => this.delete(key))
        }
    })

    Object.defineProperty(this, "store", {
        get: () => store
    })

    Object.defineProperty(this, "order", {
        get: () => order
    })

    Object.defineProperty(this, "size", {
        get: () => Object.keys(this.store).length
    });

    Object.defineProperty(this, "delete", {
        get: () => (key) => {
            if (key in this.store) {
                delete this.store[key];
                delete this[key];
                this.order.splice(this.order.indexOf(key), 1);
                return true;
            }

            let desc = Object.getOwnPropertyDescriptor(this, key) || {configurable: true};
            return desc.configurable;
        }
    })

    for (let [key, value] of Object.entries(init))
        this.cache(key, value);
}

LRUCache.prototype.cache = function (key, value) {
    if (this.size === this.capacity)
        this.delete(this.order.shift());

    if (this.order.includes(key))
        this.order.splice(this.order.indexOf(key), 1);

    this.order.push(key);
    this.store[key] = value;

    Object.defineProperty(this, key, {
        configurable: true,
        enumerable: true,
        get: () => this.store[key],
        set: (v) => this.cache(key, v),
    })

    return this;
}