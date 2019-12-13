function getArgs(func) {
    return (func + '')
        .replace(/[/][/].*$/mg, '')
        .replace(/\s+/g, '')
        .replace(/[/][*][^/*]*[*][/]/g, '')
        .split('){', 1)[0].replace(/^[^(]*[(]/, '')
        .replace(/=[^,]+/g, '')
        .split(',').filter(Boolean);
}

let DI = function (dependency) {
    this.dependency = dependency;
};

DI.prototype.inject = function (func) {
    return () => func(...getArgs(func).map(arg => this.dependency[arg]));
};