braces = '(){}[]'


def validBraces(string):
    stack = []
    for s in string:
        if not braces.index(s) % 2:
            stack.append(s)
        elif not stack or braces.index(s) - braces.index(stack[-1]) != 1:
            return False
        else:
            stack.pop()

    return not stack