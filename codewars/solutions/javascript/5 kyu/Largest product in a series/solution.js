let greatestProduct = input => Math.max(
    ...[...input.slice(0, -4)]
        .map((_, i) => [...input.slice(i, i + 5)])
        .map(arr => arr.reduce((a, b) => a * parseInt(b), 1))
);