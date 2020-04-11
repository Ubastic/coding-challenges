let cache = func => {
  let _cache = new Map();
  return (...args) => {
    let key = JSON.stringify(args);
    if (!_cache.has(key))
      _cache.set(key, func(...args));
    return _cache.get(key);
  }
}