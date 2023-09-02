from functools import partial
from operator import itemgetter


x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('Jonh', 'Backus')
]

# partial Принимает функцию и ее именованные атрибуты, чтобы можно было вызывать новую функцию не передовая эти атрибуты
sort_dy_last = partial(list.sort, key=itemgetter(-1))
print(x)

sort_dy_last(x)
print(x)

y = ['sab', 'saa', 'sac']
sort_dy_last(y)
print(y)
