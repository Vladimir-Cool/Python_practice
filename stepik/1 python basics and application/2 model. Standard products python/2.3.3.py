from itertools import takewhile

def count_divisors(num):
    for el in range(2, num):
        if num % el == 0:
            return False
    return True

def primes():
    num = 1
    while True:
        num += 1

        if count_divisors(num):
            yield num

print(list(takewhile(lambda x: x <= 31, primes())))


"""
Генератор, но не бесконечный а только до 100 
"""

z = (x for x in range(100) if count_divisors(x))

print(next(z))

