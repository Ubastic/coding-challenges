let topThreeWords = text => {
    let stats = {};

    text.toLowerCase()
        .replace(
            /[a-z0-9']+/g,
            word => word !== "'" ? stats[word] = (stats[word] || 0) + 1 : ""
        );

    return Object
        .keys(stats)
        .sort((a, b) => stats[b] - stats[a])
        .slice(0, 3);
};