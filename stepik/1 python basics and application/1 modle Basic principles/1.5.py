
class Buffer:
    def __init__(self):
        self.line = []

    def add(self, *a):
        self.line += a
        while len(self.line) >= 5:
            print(sum(self.line[0:5]))
            self.line = self.line[5:len(self.line)]

    def get_current_part(self):
        return self.line

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()