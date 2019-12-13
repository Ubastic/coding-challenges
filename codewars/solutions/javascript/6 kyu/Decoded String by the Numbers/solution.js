function decode(str) {
    let array = [...str];
    let result = [];

    while (array.length > 0) {
        if (array[0] === '\\') {
            array.shift();
            let number = '';
            while ('0' <= array[0] && array[0] <= '9') {
                number += array.shift();
            }
            result.push(array.splice(0, parseInt(number)).join(''));
        } else {
            result.push(array.shift());
        }
    }

    return result;
}
