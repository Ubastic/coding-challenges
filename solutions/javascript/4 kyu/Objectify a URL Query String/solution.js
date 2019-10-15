let namespace = (root, path, value) => {
    let fields = path.split('.'), cur = root;
    fields.forEach((field, i) => cur = cur[field] = i === fields.length - 1 ? value : cur[field] || {});
    return root;
};

let parseQuery = queryString => queryString.split('&')
    .map(s => s.split('='))
    .reduce((root, [key, value]) => {
        namespace(root, decodeURIComponent(key), decodeURIComponent(value));
        return root;
    }, {});

let convertQueryToMap = query => query.length === 0 ? "" : parseQuery(query);