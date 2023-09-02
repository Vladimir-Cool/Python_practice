
def checkpolindrom(N):
    pay = 0
    for i in range(len(N) // 2):
        if N[i] != N[-i - 1]:
            N[-i - 1] = N[i]
            pay += 1
    return pay

N = list(input())
print(checkpolindrom(N))
