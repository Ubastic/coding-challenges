let createOperator = (name, op) => {
    class Operation extends Value {
        constructor(left, right) {
            super();
            this.left = left;
            this.right = right;
        }

        ["eval"]() {
            return new Value(op(this.left.eval(), this.right.eval()));
        }

        toString() {
            return `${this.left} ${name} ${this.right}`;
        }
    }

    return Operation;
};