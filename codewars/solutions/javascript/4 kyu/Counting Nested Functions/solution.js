let stackDepth = () => new Error().stack.split("\n").length;


class CallStackExplorer {
    constructor() {
        this.depth = 0;
    }

    valueOf() {
        this.depth = stackDepth() - 2;
        return 0;
    };
}

let unnest = f => {
    Error.stackTraceLimit = Infinity;
    let c = new CallStackExplorer();

    f(c);

    return c.depth - stackDepth();
};