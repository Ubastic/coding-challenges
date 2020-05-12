String.prototype.reminder = function () {
    return this.split('.')[1].length;
}

String.prototype.asFloat = function () {
    return this.includes(".") ? this : this + ".0";
}

String.prototype.insert = function (index, item) {
    return [...this.slice(0, this.length - index), item, ...this.slice(this.length - index)].join("");
};

let sumStrings = (a, b) => {
    a = [...a.padStart(Math.max(a.length, b.length), "0")].reverse();
    b = [...b.padStart(Math.max(a.length, b.length), "0")].reverse();

    let remainder = 0, value = "";
    for (let i = 0; i < a.length; i++) {
        let n = parseInt(a[i]) + parseInt(b[i]) + remainder;
        [remainder, value] = [Math.floor(n / 10), `${n % 10}${value}`];
    }

    return `${remainder}${value}`;
};

let addTwo = (a, b) => {
    let numbers = [a, b].map(n => n.toString().asFloat());
    let dotLen = Math.max(...numbers.map(s => s.reminder()));
    numbers = numbers.map(n => n + "0".repeat(dotLen - n.reminder())).map(n => n.replace('.', ''));
    return sumStrings(...numbers).insert(dotLen, ".").replace(/^0+(?=\d)|\.?0+$/g, '');
}

let add = (...args) => {
    let numbers = args.map(n => n.toString().asFloat());
    return numbers.some(n => !(/\d+(\.\d+)?/g).test(n)) ? NaN : numbers.reduce(addTwo);
}