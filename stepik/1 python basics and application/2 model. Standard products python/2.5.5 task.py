from operator import mod
from functools import partial

y = 3
x = 3

def mod_checker(x, mod=0):
    return lambda y: y % x == mod




test = mod_checker(3, 1)
print(test(3))
print(test(4))

test2 = mod_checker(4)
print(test2(3))
print(test2(4))






