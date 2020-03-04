let sumStrings = (a, b) => {
    a = [...a.padStart(Math.max(a.length, b.length), "0")].reverse();
    b = [...b.padStart(Math.max(a.length, b.length), "0")].reverse();

    let remainder = 0, value = "";
    for (let i = 0; i < a.length; i++) {
        let n = parseInt(a[i]) + parseInt(b[i]) + remainder;
        value = `${n % 10}${value}`;
        remainder = Math.floor(n / 10);
    }

    return `${remainder}${value}`.replace(/^0+/, '');
};