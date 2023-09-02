

"""
Итератор - функция __next__ возвращает элементы переданного итерируемого объекта
"""
class MyIterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1

            return self.iterable[self.index - 1]
        raise StopIteration


class MyList:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return MyIterator(self.lst)


l = MyList([1, 2, 3, 4])
print(type(l))
for i in l:
    print(i)