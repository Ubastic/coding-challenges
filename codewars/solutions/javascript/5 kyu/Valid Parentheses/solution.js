let validParentheses = parens => {
    let stack = [];
    for (let p of parens) {
        if (p === "(")
            stack.push("(");
        else if (!stack.length || stack[stack.length - 1] !== "(")
            return false;
        else
            stack.pop();
    }
    return !stack.length;
};
