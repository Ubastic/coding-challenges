let format = (tags = []) => {
    let callback = (...args) => (
        tags.map(t => `<${t}>`).join('') + args.join('') + tags.reverse().map(t => `</${t}>`).join('')
    );

    for (let tag of ['div', 'h1', 'p', 'span'])
        Object.defineProperty(callback, tag, {get: () => format([...tags, tag])});

    return callback;
}

let Format = format();