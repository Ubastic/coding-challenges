let toBSTArray = array => {
    let bst = [];
    let add = (value, root = 0) => {
        if (bst[root] === undefined)
            bst[root] = value;
        else if (value < bst[root])
            add(value, 2 * root + 1);
        else
            add(value, 2 * root + 2);
    };
    array.forEach(i => add(i));

    return bst;
};

let isBSTArray = (array, root = 0, min = Number.NEGATIVE_INFINITY, max = Number.POSITIVE_INFINITY) =>
    array[root] === undefined || (
        min <= array[root] && array[root] <= max
        && isBSTArray(array, 2 * root + 1, min, array[root])
        && isBSTArray(array, 2 * root + 2, array[root], max)
    );

let toArray = bst => {
    if (!isBSTArray(bst))
        throw new Error('The parameter must be a BSTArray');

    let array = [];
    let travels = (root = 0) => {
        if (bst[root] === undefined)
            return;

        travels(2 * root + 1);
        array.push(bst[root]);
        travels(2 * root + 2);
    };
    travels();

    return array;
};