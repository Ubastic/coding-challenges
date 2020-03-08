let findDuplicates = arr => {
    let dups = 1;
    for (let i = 1; i < arr.length; i++, dups++)
        if (arr[i] !== arr[0])
            break;

    if (dups < 3)
        return [0, null];

    return [dups, `${arr[0]}:${dups}`];
};

let findSequence = arr => {
    let step = arr[1] - arr[0], seq = 2, additional = [], total;

    for (let i = 1; i < arr.length - 1; i++, seq++)
        if (arr[i + 1] - arr[i] !== step)
            break;

    if (seq < 3)
        return [0, null];

    total = seq;
    let [next_seq, res] = findSequence(arr.slice(seq - 1));

    if (seq > 3 && next_seq === 3) {
        [seq, total, additional] = [seq - 1, total + next_seq - 1, [res]];
    }

    step = step < 0 ? step : `+${step}`;
    return [total, [`${arr[0]}:${seq}${step}`, ...additional].join()];
};

let findOne = arr => [1, `${arr[0]}`];

let arrayToString = arr => {
    let res = [], skip, part;

    while (arr.length) {
        for (let folder of [findDuplicates, findSequence, findOne]) {
            [skip, part] = folder(arr);
            if (skip !== 0) break;
        }
        res.push(part);
        arr.splice(0, skip);
    }

    return res.join();
};

let stringToArray = str => str.split(",").map(s => {
    if (s.match(/^\d+$/)) {
        return [parseInt(s)];
    } else if (s.match(/^[+-]?\d+:[+-]?\d+$/)) {
        let [n, c] = s.match(/[+-]?\d+/g).map(i => parseInt(i));
        return Array(c).fill(parseInt(n));
    } else {
        let [start, c, step] = s.match(/[+-]?\d+/g).map(i => parseInt(i));
        return Array(c).fill(0).map((_, i) => start + step * i);
    }
}).reduce((acc, arr) => [...acc, ...arr], []);