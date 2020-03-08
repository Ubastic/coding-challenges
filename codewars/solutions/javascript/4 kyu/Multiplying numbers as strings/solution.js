String.prototype.replaceZeros = function () {
    return this.replace(/^0+/, '') || "0";
};

let divMod = (a, b = 10) => [Math.floor(a / b), a % b];

let digits = (a, b) => Array(Math.max(a.length, b.length))
    .fill(0)
    .map((_, i) => [a[a.length - 1 - i] || "0", b[b.length - 1 - i] || "0"])
    .map(arr => arr.map(i => parseInt(i)));

let add = (a, b) => {
    let remainder = 0, value = "", n;

    for (let [x, y] of digits(a, b)) {
        [remainder, n] = divMod(x + y + remainder);
        value = `${n}${value}`;
    }

    return `${remainder}${value}`.replaceZeros();
};

let multiply = (a, b) => {
    [a, b] = [a.replaceZeros(), b.replaceZeros()];

    if (a === "0" || b === "0")
        return "0";

    [a, b] = a.length > b.length ? [a, b] : [b, a];

    if (b.length === 1) {
        let remainder = 0, value = "", n;
        for (let [x,] of digits(a, b)) {
            [remainder, n] = divMod(x * parseInt(b) + remainder);
            value = `${n % 10}${value}`;
        }

        return `${remainder}${value}`.replaceZeros();
    }

    return [...b]
        .reverse()
        .reduce((acc, x, i) => add(acc, multiply(a, x) + "0".repeat(i)), "0")
        .replaceZeros();
};