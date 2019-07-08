def valid_parentheses(string):
    stack = []
    for c in string:
        if c == ')':
            if not stack:
                return False

            stack.pop()

        elif c == '(':
            stack.append(c)

    return not stack