const priority = {'-': 0, '+': 0, '*': 1, '/': 1};
const executors = {
    '-': (a, b) => a - b,
    '+': (a, b) => a + b,
    '*': (a, b) => a * b,
    '/': (a, b) => a / b,
};

class Calculator {
    evaluate(string) {
        let rpn = [];
        let ops = [];

        for (let t of string.match(/[+\-*\/]|[0-9]+/g)) {
            if (t in priority) {
                while (ops.length && priority[ops[ops.length - 1]] >= priority[t]) {
                    rpn.push(ops.pop());
                }
                ops.push(t);
            } else {
                rpn.push(parseFloat(t));
            }
        }
        rpn.push(...ops.reverse());

        let stack = [];
        while (rpn.length) {
            let t = rpn.shift();

            if (t in executors) {
                stack.push(executors[t](...[stack.pop(), stack.pop()].reverse()));
            } else {
                stack.push(t);
            }
        }

        return stack[0];
    }
}