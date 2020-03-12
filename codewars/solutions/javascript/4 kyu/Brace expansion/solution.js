let expandBraces = str => {
    let match = str.match(/{([^{}]*?)}/);

    if (match === null)
        return [str];

    let [first, ...others] = match[1]
        .split(",")
        .map(s => expandBraces(str.replace(match[0], s)));

    return first.reduce(
        (
            (acc, s, i) => first.length > 1 && others.every(c => c[i] === s)
                ? [...acc, s]
                : [...acc, first[i], ...others.map(c => c[i])]
        ), []
    );
};