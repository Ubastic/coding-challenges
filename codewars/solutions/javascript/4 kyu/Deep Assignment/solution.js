let deepAssignment = (obj, keyPath, value) => {
    let parts = keyPath.match(/[a-zA-Z_]+|\d+/g).map(s => s.match(/\d+/g) ? parseInt(s) : s);
    let getNext = (current, i) => {
        let next = Number.isInteger(parts[i + 1]) ? [] : {};
        return current !== undefined && Array.isArray(next) === Array.isArray(current) ? current : next;
    };
    parts.slice(0, -1).reduce(
        (acc, attr, i) => acc[attr] = getNext(acc[attr], i), obj
    )[parts[parts.length - 1]] = value;
};
