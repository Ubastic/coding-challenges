String.prototype.replaceZeros = function () {
    return this.replace(/^0+/, '') || "0";
};

function* digits(a, b) {
    a = [...a.padStart(Math.max(a.length, b.length), "0")].reverse();
    b = [...b.padStart(Math.max(a.length, b.length), "0")].reverse();

    for (let i = 0; i < a.length; i++)
        yield [parseInt(a[i]), parseInt(b[i])]

}

let sub = (a, b) => {
    let remainder = 0, value = "";

    for (let [x, y] of digits(a, b)) {
        x -= remainder;

        if (x < y) {
            x += 10;
            remainder = 1;
        } else {
            remainder = 0;
        }

        let n = x - y;
        value = `${n}${value}`;
    }

    return `${remainder}${value}`.replaceZeros();
};

let add = (a, b) => {
    let remainder = 0, value = "";

    for (let [x, y] of digits(a, b)) {
        let n = x + y + remainder;
        value = `${n % 10}${value}`;
        remainder = Math.floor(n / 10);
    }

    return `${remainder}${value}`.replaceZeros();
};

let greater = (a, b, equal = true) => {
    if (equal && a === b)
        return true;

    for (let [x, y] of [...digits(a, b)].reverse()) {
        if (x > y)
            return true;
        else if (y > x)
            return false;
    }

    return true;
};

let divideStrings = (a, b) => {
    if (greater(b, a, false))
        return ["0", a];

    let part = a.slice(0, b.length);

    while (!greater(part, b))
        part = a.slice(0, part.length + 1);

    let parts = [...a.slice(part.length)];
    let quotient = "";

    while (true) {
        let loc_quotient = "0";
        while (greater(part, b)) {
            part = sub(part, b);
            loc_quotient = add(loc_quotient, "1");
        }
        quotient += loc_quotient;

        if (!parts.length)
            break;

        part += parts.shift();
    }

    return [quotient.replaceZeros(), part.replaceZeros()]
};