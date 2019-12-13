def calculate(a, o, b):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "/" and b != 0:
        return a / b
    elif o == "*":
        return a * b