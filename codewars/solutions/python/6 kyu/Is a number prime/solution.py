def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, num))
