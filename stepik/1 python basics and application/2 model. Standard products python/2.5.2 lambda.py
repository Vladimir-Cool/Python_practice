
x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('Jonh', 'Backus')
]

# Определяет сколько в имени (в кортеже) букв
# def lenght(name):
#     return len(' '.join(name))
#
# name_length = [lenght(name) for name in x]
# print(name_length)
#
# x.sort(key=lenght)
# print(x)
#______________________________________________________
# Можно не создавать отдельно функцию если тело функции помещаеться в выражение
x.sort(key=lambda name: len(' '.join(name)))
print(x)
