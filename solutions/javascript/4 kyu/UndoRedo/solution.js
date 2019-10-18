class States {

    constructor(object) {
        this.object = object;
        this.reduStates = [];
        this.undoStates = [];
    }

    setState(source) {
        Object.keys(this.object).forEach(prop => delete this.object[prop]);
        Object.assign(this.object, source);
    }

    set(key, value) {
        this.reduStates.length = 0;
        this.undoStates.push(Object.assign({}, this.object));
        this.object[key] = value;
    }

    get(key) {
        return this.object[key];
    }

    del(key) {
        this.reduStates.length = 0;
        this.undoStates.push(Object.assign({}, this.object));
        delete this.object[key];
    }

    undo() {
        if (this.undoStates.length === 0) {
            throw new Error();
        }

        let state = this.undoStates.pop();
        this.reduStates.push(Object.assign({}, this.object));
        this.setState(state);
    }

    redo() {
        if (this.reduStates.length === 0) {
            throw new Error();
        }

        let state = this.reduStates.pop();
        this.undoStates.push(Object.assign({}, state));
        this.setState(state);
    }
}

let undoRedo = object => new States(object);
