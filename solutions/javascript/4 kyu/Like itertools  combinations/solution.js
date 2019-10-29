function* icombinations(arr, k) {
    if (arr.length < k) {
        return null;
    } else if (k === 1) {
        yield* arr.map(i => [i]);
    } else {
        for (let i = 0; i < arr.length; i++) {
            for (let j of icombinations(arr.slice(i + 1, arr.length), k - 1)) {
                yield [arr[i], ...j];
            }
        }
    }
}