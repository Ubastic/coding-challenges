let extend = (...args) => Object.assign({}, ...args.filter(obj => isObject(obj)).reverse());