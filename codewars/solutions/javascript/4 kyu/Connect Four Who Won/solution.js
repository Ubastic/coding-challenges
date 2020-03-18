let rotate = board => board[0].map((col, i) => board.map(row => row[i]));
let flip = board => board.map(b => [...b].reverse());

let diagonal = board => board
    .map((_, i) => board
        .slice(i)
        .map((_, j) => board.slice(i).map((d, ii) => d[j + ii]).map(a => a || "-"))
        .filter(row => row.length >= 4)
    ).reduce((acc, a) => [...acc, ...a], []);

let contains = (board, line) =>
    [board, rotate(board), diagonal(board), diagonal(flip(board))]
        .reduce((acc, a) => [...acc, ...a], [])
        .some(b => b.join("").includes(line));

let connectFour = board => {
    let [red, yellow] = ['R', 'Y'].map(player => contains(board, player.repeat(4)));
    let empty = !board.reduce((acc, a) => [...acc, ...a], []).join("").includes("-");

    return yellow ? "Y" : red ? "R" : empty ? "draw" : "in progress";
};