def all_fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b