let distance = (x1, y1, x2, y2) => Math.sqrt((x1 - x2) ** 2) + Math.sqrt((y1 - y2) ** 2);

let closestPair = points => points
    .map((p1, i) => points.slice(i + 1).map(p2 => [p1, p2]))
    .reduce((acc, a) => [...acc, ...a], [])
    .sort((a, b) => distance(...a[0], ...a[1]) - distance(...b[0], ...b[1]))[0];
