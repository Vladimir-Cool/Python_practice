
class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, item: int) -> None:
        if item > 0:
           super().append(item)
        else:
            raise NonPositiveError('Число ', item, ' Должно быть больше положительным')


l = PositiveList()
l.append(4)
print(l)
l.append(-2)

