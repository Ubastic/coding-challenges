function CurryIt(func) {
    let [fixedArgs, objThis] = [[], null];
    return function (...args) {
        objThis = this !== global ? this : objThis;
        if (args.length === 0) {
            let r = func.call(objThis, ...fixedArgs);
            fixedArgs.length = 0;
            return r;
        }
        fixedArgs.push(...args);
        return this;
    }
}