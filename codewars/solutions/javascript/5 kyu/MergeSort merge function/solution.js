let mergesorted = (a, b) => {
    let res = [];
    while (a.length > 0 && b.length > 0) {
        res.push(a[0] < b[0] ? a.shift() : b.shift());
    }
    return [...res, ...a, ...b];
};
