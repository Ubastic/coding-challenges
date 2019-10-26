const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'];

class Value {
    constructor(value) {
        this.value = value;
        this.operations = {
            plus: a => value + a,
            minus: a => value - a,
            times: a => value * a,
            dividedBy: a => value / a
        };
        return new Proxy(this, this);
    }

    get(target, prop) {
        return prop in this.operations ? new Stage(this.operations[prop]) : this[prop];
    }

    [Symbol.toPrimitive]() {
        return this.value;
    }
}

class Stage {
    constructor(parent) {
        this.parent = parent || (a => a);
        return new Proxy(this, this);
    }

    get(target, prop) {
        return numbers.includes(prop) ? new Value(this.parent(numbers.indexOf(prop))) : this[prop];
    }
}

let FluentCalculator = new Stage();
