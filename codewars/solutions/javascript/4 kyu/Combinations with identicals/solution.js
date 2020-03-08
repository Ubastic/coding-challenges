// This code is translation of Python code:
// https://stackoverflow.com/a/36430061/12243670
let counter = arr => {
    let stats = new Map();
    for (let i of arr) {
        stats.set(i, stats.has(i) ? stats.get(i) + 1 : 1);
    }
    let values = [], counts = [];
    for (let [value, count] of stats.entries()) {
        values.push(value);
        counts.push(count);
    }
    return [values, counts];
};

function* repeat(value, n) {
    for (let i = 0; i < n; i++)
        yield value
}

function* chain(...iterables) {
    for (let iterable of iterables)
        yield* iterable;
}

function* slice_start(iterable, n) {
    let iterator = iterable[Symbol.iterator]();

    for (let i = 0; i < n; i++)
        iterator.next();

    while (true) {
        let next = iterator.next();

        if (next.done)
            break;

        yield next.value;
    }
}

function* slice_stop(iterable, n) {
    let iterator = iterable[Symbol.iterator]();

    for (let i = 0; i < n; i++) {
        let next = iterator.next();
        if (next.done)
            break;

        yield next.value;
    }
}

function* map(func, ...iterables) {
    for (let args of zip(...iterables))
        yield func(...args);
}

function* count(n = 0) {
    while (true) {
        yield n;
        n++;
    }
}

function* zip(...iterables) {
    let iterators = iterables.map(i => i[Symbol.iterator]());

    while (true) {
        let values = iterators.map(i => i.next());

        if (values.some(i => i.done))
            break;

        yield values.map(i => i.value);
    }
}

function* reversed(iterable) {
    yield* [...iterable].reverse();
}

function* range(...args) {
    let [start, end] = args.length === 2 ? args : [0, ...args];

    while (start < end) {
        yield start;
        start++;
    }
}

function* combineWithoutRepetitions(arr, r) {
    let [values, counts] = counter(arr);

    let f = (i, c) => chain(...map(repeat, i, c));

    let n = counts.length;
    let indices = [...slice_stop(f(count(), counts), r)];

    if (indices.length < r)
        return;

    while (true) {
        yield indices.map(i => values[i]).sort();

        let flag = false, i;
        for (let [ii, jj] of zip(reversed(range(r)), f(reversed(range(n)), reversed(counts)))) {
            if (indices[ii] !== jj) {
                flag = true;
                i = ii;
                break
            }
        }

        if (!flag)
            return;

        let j = indices[i] + 1;

        for (let [ii, jj] of zip(range(i, r), f(count(j), slice_start(counts, j, null))))
            indices[ii] = jj
    }
}

Array.prototype.combinations = function (n) {
    if (!Number.isInteger(n) || n < 0)
        throw Error();

    return [...combineWithoutRepetitions(this, n)];
};