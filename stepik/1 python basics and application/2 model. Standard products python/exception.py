"""
Исключение работает для вылавливания TypeError
"""
try:
    listexample = [6, 1, -4, 'str']
    listexample.sort()
    print(listexample)
except TypeError:
    print('Ошибка сортировки')

"""
Исключение не работает c картежем.
"""
def func1(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError) as error:
        print(error)
        print(type(error))
        print(error.args)

func1(4, [])
func1(4, 0)

print('Вывод текста после ошибки')


"""
Под капотом
"""
try:
    15/0
    #e
except ZeroDivisionError: # isinstance(e, ZeroDivisionError) == True
    print('Ошибка деления на ноль')

"""
Наследование классов ошибок.
"""
print(ZeroDivisionError.mro())

try:
    15/0
    #e
except ArithmeticError: # isinstance(e, ArithmeticError) == True
    print('Арифметическая ошибка')

"""
else Исполняеться если не выловлено исключений
finaly Исполняеться после всего блока try
"""

def func2(x, y):
    try:
        resalt = x / y
    except (ZeroDivisionError):
        print('Делить на ноль, нельзя')
    else:
        print('Результат', resalt)
    finally:
        print('print finally')

func2(2, 1)
func2(2, 0)
func2(2, {})
