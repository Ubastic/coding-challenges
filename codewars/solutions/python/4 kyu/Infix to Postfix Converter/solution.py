PRECEDENCE = {'^': 9, '*': 7, '/': 7, '+': 5, '-': 5, '(': 1, ')': 1}


def to_postfix(expression_phrase):
    stack, output = [], []
    for c in expression_phrase:
        if c not in PRECEDENCE:
            output.append(c)
        elif c not in '()':
            while stack and PRECEDENCE[c] <= PRECEDENCE[stack[-1]]:
                output.append(stack.pop())
            stack.append(c)
        elif c == '(':
            stack.append(c)
        else:
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    return ''.join(output + stack[::-1])