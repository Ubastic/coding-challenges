let canAttack = ([x1, y1], [x2, y2]) => x1 === x2 || y1 === y2 || Math.abs(x1 - x2) === Math.abs(y1 - y2);

let isValid = queue => {
    for (let i = 0; i < queue.length; i++)
        for (let j = i + 1; j < queue.length; j++)
            if (canAttack(queue[i], queue[j]))
                return false;

    return true;
}

let solve = (queue, size, lastRow) => {
    if (queue.length === size)
        return queue;

    for (let i = lastRow; i < size; i++)
        for (let j = 0; j < size; j++) {
            let newQueue = [...queue, [i, j]];

            if (isValid(newQueue)) {
                let result = solve(newQueue, size, i);

                if (result)
                    return result;
            }
        }
}

const [X_POS, Y_POS] = ["abcdefghij", "1234567890"];

let queens = ([x, y], size) => solve([[X_POS.indexOf(x), Y_POS.indexOf(y)]], size, 0)
    .map(([x, y]) => X_POS[x] + Y_POS[y])
    .join();