function solve_graph(start, end, arcs) {
    let edges = {};
    for (let node of arcs) {
        edges[node.start] = [...(edges[node.start] || []), node.end];
    }
    let queue = [start];
    let visited = [start];

    while (queue.length > 0) {
        (edges[queue.shift()] || []).filter(n => !visited.includes(n))
            .forEach(n => {visited.push(n);queue.push(n)});

        if (visited.includes(end)) {
            return true;
        }
    }
    return false;
}