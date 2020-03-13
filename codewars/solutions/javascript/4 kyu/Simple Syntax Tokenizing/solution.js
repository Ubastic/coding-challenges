let valid_braces = tokens => {
    while (tokens.includes('()'))
        tokens = tokens.replace('()', '');
    return tokens.length === 0;
};

function* parts(tokens) {
    let s = "";
    while (tokens.length > 0) {
        let c = tokens.shift();

        if (c === "(") {
            yield s;
            s = "";

            let end = 0, brackets = 1;
            for (let i = 0; i < tokens.length && brackets !== 0; i++, end++)
                brackets += [1, -1]["()".indexOf(tokens[i])] || 0;

            yield [tokens.splice(0, end).slice(0, -1).join("")]
        } else s += c;
    }

    if (s.length) yield s
}


let tokenise = string => {
    return !valid_braces(string.replace(/[^()]/g, '')) ? null : [...parts([...string])]
        .map(s => Array.isArray(s) ? [tokenise(...s)] : s.match(/[!#$%&*+\-\/<=>@^_.,;]+|[a-zA-Z]+/g) || [])
        .reduce((acc, s) => [...acc, ...s], []);
};