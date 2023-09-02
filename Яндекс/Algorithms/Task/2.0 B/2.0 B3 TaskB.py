
def findornot(N):
    D = dict()
    for i in range(len(N)):
        if N[i] not in D:
            D[N[i]] = 0
            print('NO')
        else:
            print('YES')


N = input().split()
findornot(N)
