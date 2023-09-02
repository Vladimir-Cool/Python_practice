
def datedefinition(x, y):
    if x == y:
        return "1"
    elif x < 13 and y < 13:
        return "0"
    return "1"

x, y, z = map(int, input().split())

print(datedefinition(x, y))
