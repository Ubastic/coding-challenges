function* _permutations(a) {
    if (a.length === 1) {
        yield a;
    } else {
        for (let i = 0; i < a.length; i++) {
            for (let e of _permutations([...a.slice(0, i), ...a.slice(i + 1)])) {
                yield [a[i], ...e];
            }
        }
    }
}

let permutations = s => [...new Set([..._permutations([...s])].map(a => a.join("")))];
