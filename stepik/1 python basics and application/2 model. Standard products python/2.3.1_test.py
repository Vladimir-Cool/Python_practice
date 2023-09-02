
class DoubleElementListIterator:

    def __init__(self, lst):
        self.lst = lst
        self.count = 0

    def __next__(self):
        if self.count < len(self.lst):
            self.count += 2
            return self.lst[self.count - 2], self.lst[self.count - 1]
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

for pair in MyList([1, 2, 3, 4]):
    print(pair)