
def onlyone(N):
    D = dict()
    ans = []
    for i in range(len(N)):
        if N[i] not in D:
            D[N[i]] = 0
        else:
            D[N[i]] += 1
    for i in range(len(N)):
        if D[N[i]] == 0:
            ans.append(N[i])
    return ' '.join(ans)

N = input().split()
print(onlyone(N))
