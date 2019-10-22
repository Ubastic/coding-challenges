let findVisited = edges => {
    let start = Object.keys(edges)[0];

    let queue = [start];
    let visited = [start];

    while (queue.length > 0) {
        (edges[queue.shift()] || [])
            .filter(n => !visited.includes(n))
            .forEach(n => {
                visited.push(n);
                queue.push(n)
            });
    }
    return visited;
};

function countDistricts(city) {
    let districts = [];

    while (Object.keys(city).length > 0) {
        let district = findVisited(city);
        district.forEach(key => delete city[key]);
        districts.push(district);
    }

    return districts.length;
}