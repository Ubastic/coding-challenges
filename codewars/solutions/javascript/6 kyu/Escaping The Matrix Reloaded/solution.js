class Neo extends Error {
    constructor() {
        super();
        this.name = "Neo";
    }
}

const Matrix = {enter: () => {throw new Neo()}};