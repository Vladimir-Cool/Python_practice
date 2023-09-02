'''Не проходит 26 тест'''

def Itog(r:int, i:int, c:int) -> int:
    if i == 0:
        if r != 0:
            return 3
        else:
            return c
    elif i == 1:
        return c
    elif i == 4:
        if r != 0:
            return 3
        else:
            return 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    return i

a = int(input())
b = int(input())
c = int(input())

print(Itog(a, b, c))



