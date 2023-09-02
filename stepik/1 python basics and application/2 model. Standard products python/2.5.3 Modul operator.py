from operator import add, mul, contains, itemgetter, attrgetter

print(add(4, 5))
print(mul(4, 5))
print(contains([1, 3, 4], 5))


x = [1, 3, 4]
# функция возвращает елемент по индексу
f = itemgetter(1) # f(x) ++ x[1]
print(f(x))

# функция возвращает атребут экземпляра класса
f2 = attrgetter('sort') # f2(x) == x.sort
print(f2([]))
