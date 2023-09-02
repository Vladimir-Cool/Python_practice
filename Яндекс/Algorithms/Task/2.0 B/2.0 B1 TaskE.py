
def pointcheck(d, x, y):
    if x < 0:
        if y <= d / 2:
            return 1
        else:
            return 3
    if y < 0:
        if x <= d / 2:
            return 1
        else:
            return 2
    if x + y <= d:
        return 0
    else:
        if x - y >= 0:
            return 2
        return 3


d = int(input())
x, y = map(int, input().split())

print(pointcheck(d, x, y))