let shuffle = a => {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

Object.prototype.random = function () {
    let arr = this.toRandomArray();
    return arr[Math.floor(Math.random() * arr.length)];
};

Object.prototype.toRandomArray = function () {
    let arr = [];

    Object.entries(this).map(([key, value]) => {
        arr.push(...(typeof value === "object" ? value.toRandomArray() : [value]))
    });

    return shuffle(arr);
};