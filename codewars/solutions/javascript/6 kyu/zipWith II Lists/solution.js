let isInfinite = node => {
    let nodes = new Set();

    while (node) {
        if (nodes.has(node))
            return true;
        nodes.add(node);
        node = node.next;
    }

    return false;
}

let zipWith = (fn, h0, h1) => {
    let root, prev;

    if (isInfinite(h0) && isInfinite(h1))
        throw new Error();

    while (h0 && h1) {
        let node = new Node(fn(h0.value, h1.value));
        if (prev) prev.next = node;
        [h0, h1, prev, root] = [h0.next, h1.next, node, root || node];
    }

    return root;
}