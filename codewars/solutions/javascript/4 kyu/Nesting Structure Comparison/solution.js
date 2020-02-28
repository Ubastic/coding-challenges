Array.prototype.sameStructureAs = function (other) {
    let compare = a => Array.isArray(a) ? a.map(compare) : 0;
    return JSON.stringify(compare(this)) === JSON.stringify(compare(other));
};