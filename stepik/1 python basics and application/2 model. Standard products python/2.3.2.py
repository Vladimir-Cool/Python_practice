
class multifilter():
    def judge_any(self, pos, neg):
        if pos >= 1:
            return True

    def judge_half(self, pos, neg):
        if pos >= neg:
            return True

    def judge_all(self, pos, neg):
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge=None):
        self.iterable = iterable
        self.funcs = funcs
        self.index = 0
        self.judge = judge or multifilter.judge_any

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            while self.index < len(self.iterable):
                self.index += 1
                pos = 0
                neg = 0
                for f in self.funcs:
                    if f(self.iterable[self.index - 1]):
                        pos += 1
                    else:
                        neg += 1

                if self.judge(self, pos, neg):
                        return self.iterable[self.index - 1]
        raise StopIteration


# Примеры для проверки
def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30
print(list(multifilter(a, mul2, mul3, mul5)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]