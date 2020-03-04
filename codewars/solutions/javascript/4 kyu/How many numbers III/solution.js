String.prototype.sum = function () {
    return [...this].map(s => parseInt(s)).reduce((a, b) => a + b, 0);
};

function* numbers(digits, start = 1) {
    if (digits === 1)
        for (let i = start; i < 10; i++)
            yield `${i}`;
    else
        for (let i = start; i < 10; i++)
            for (let j of numbers(digits - 1, i))
                yield `${i}${j}`;
}

let findAll = (n, k) => {
    if ("9".repeat(k).sum() < n)
        return [];

    let all = [...numbers(k)].filter(s => s.sum() === n);
    return [all.length, all[0], all[all.length - 1]];
};