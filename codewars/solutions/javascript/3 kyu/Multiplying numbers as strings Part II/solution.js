let divideOnParts = s => {
    let [digit, float] = s.includes(".") ? s.split(".") : [s, "0"];
    return [replaceStartZeros(digit), replaceEndZeros(float)];
};

let replaceEndZeros = s => s.replace(/0+$/, '') || "0";

let replaceStartZeros = s => s.replace(/^0+/, '') || "0";

let normalize = (a, b) => [a, b].map(s => s.padEnd(Math.max(a.length, b.length), "0"));

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

    return replaceStartZeros(`${remainder}${value}`);
};

let _multiply_with_one = (a, b) => {
    let remainder = 0, value = "", n;

    for (let [x,] of digits(a, b)) {
        [remainder, n] = divMod(x * parseInt(b) + remainder);
        value = `${n % 10}${value}`;
    }

    return replaceStartZeros(`${remainder}${value}`);
};

let _multiply = (a, b) => {
    [a, b] = [replaceStartZeros(a), replaceStartZeros(b)];

    if (a === "0" || b === "0")
        return "0";

    [a, b] = a.length > b.length ? [a, b] : [b, a];

    return replaceStartZeros([...b]
        .reverse()
        .reduce((acc, x, i) => add(acc, _multiply_with_one(a, x) + "0".repeat(i)), "0"));
};

let multiply = (a, b) => {
    let sign = (a[0] === "-" || b[0] === "-") && a[0] !== b[0] ? "-" : "";
    [a, b] = [a, b].map(s => divideOnParts(s.replace(/^-/, '')));
    [a[1], b[1]] = normalize(a[1], b[1], "End");

    let res = _multiply(a.join(""), b.join(""));

    if (res === "0")
        return "0";

    let floatStart = a[1].length * 2;
    res = res.padStart(floatStart, "0");

    let digit = replaceStartZeros(res.slice(0, res.length - floatStart));
    let float = replaceEndZeros(res.slice(res.length - floatStart));

    return `${sign}${digit}.${float}`.replace(/\.0$/, '');
};