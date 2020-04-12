function LRUCache(capacity, init = {}) {
    let store = {}, order = [];

    Object.defineProperties(this, {
        size: {get: () => Object.keys(store).length},
        capacity: {
            get: () => capacity, set: (value) => {
                capacity = value;
                order.splice(0, this.size - value).forEach(key => this.delete(key))
            }
        },
        delete: {
            get: () => (key) => {
                if (key in store) {
                    delete store[key];
                    delete this[key];
                    order.splice(order.indexOf(key), 1);
                }

                return (Object.getOwnPropertyDescriptor(this, key) || {configurable: true}).configurable;
            }
        },
        cache: {
            get: () => (key, value) => {
                if (this.size === this.capacity)
                    this.delete(order.shift());

                if (order.includes(key))
                    order.splice(order.indexOf(key), 1);

                order.push(key);
                store[key] = value;

                Object.defineProperty(this, key, {
                    configurable: true,
                    enumerable: true,
                    get: () => store[key],
                    set: (v) => this.cache(key, v),
                })

                return this;
            }
        }
    });

    for (let key in init)
        this.cache(key, init[key]);
}