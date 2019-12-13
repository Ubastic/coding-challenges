let comprehension = options => {
    let g = (options.generator || "").replace(/\s/g, "");
    if (!g) {
        return [];
    } else if (!g.includes("..")) {
        return g.split(",").map(s => Number.parseInt(s));
    }

    let start, second, end, step;
    if (g.includes(",")) {
        [start, second, end] = g.split(/,|\.{2}/).map(s => Number.parseInt(s));
        step = second - start;
    } else {
        [start, end] = g.split("..").map(s => Number.parseInt(s));
        step = 1;
    }

    let arr = [];
    while (step > 0 ? start <= end : start >= end) {
        arr.push(start);
        start += step;
    }
    return arr;
};


let ArrayComprehension = options => comprehension(options)
    .filter(a => options.filters ? options.filters.every(f => f(a)) : true)
    .map(options.transform || (a => a));
