function removeZeros(array) {
    let str = '';
    let index = 0;

    for (let i = 0; i < array.length; i++) {
        if (array[i] === 0) {
            str += '0';
        } else if (array[i] === '0') {
            str += '1';
        } else {
            array[index++] = array[i];
        }
    }

    for (let i = 0, strLen = str.length; i < strLen; i++) {
        array[index++] = str[i] === '0' ? 0 : '0';
    }
    return array;
}
