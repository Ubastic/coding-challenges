Object.prototype.hash = function (string) {
    return string.split(".").reduce((obj, attr) => obj ? obj[attr] : obj , this);
}