let STEPS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

let isVisited = (arr, pos) => arr.filter(p => p[0] === pos[0] && p[1] === pos[1]).length !== 0;
let getValue = (arr, x, y) => {try {return arr[x][y];} catch (e) {return null;}};


let checkWord = (board, word) => {
    let queue = [];

    for (let [i, w] of board.entries())
        for (let [j, c] of w.entries())
            if (c === word[0])
                queue.push([word.slice(1), [i, j], [[i, j]]]);

    while (queue.length) {
        let [w, [x, y], visited] = queue.shift();

        if (w.length === 0)
            return true;

        STEPS
            .map(arr => [x + arr[0], y + arr[1]])
            .filter(pos => !isVisited(visited, pos) && getValue(board, ...pos) === w[0])
            .forEach(pos => queue.push([w.slice(1), pos, [...visited, pos]]));

    }

    return false;
};