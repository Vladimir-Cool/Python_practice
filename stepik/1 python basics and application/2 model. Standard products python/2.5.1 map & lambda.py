
#map, позволяет применить функцию int ко всем элементам последовательности ссылаясь на итератор.
#vvv = map(int, input().split())
vvv = map(int, ['10', '11', '20', '21', '30', '31'])
# x, y = map(int, input().split())
# a, b = (int(i) for i in input().split())
# print(x + y)
# print(a + b)


#filter
def even(x):
    return x % 2 == 0

even2 = lambda x: x % 2 == 0

# функция filter возвращает генератор
# result = filter(lambda x: x % 2 == 0, vvv)
# print(result)

# for el in result:
#     print(el)

# если генератор передать конструктору класса list() получим список
# Генератор нельзя использовать в 2-х циклах подряд
resultlst = list(filter(lambda x: x % 2 == 0, vvv))
print(resultlst)


