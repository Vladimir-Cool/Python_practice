def makelist() -> list:
    list = []
    i = 1
    maxnum = 0
    while i != 0:
        i = int(input())
        maxnum = max(maxnum, i)
        list.append(i)
    return [list, maxnum]
def amountmaxnum():
    list, max = makelist()
    sum = 0
    for i in range(len(list)):
        if list[i] == max:
            sum += 1
    return sum

print(amountmaxnum())

