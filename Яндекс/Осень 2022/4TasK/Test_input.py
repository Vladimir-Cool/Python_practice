
k = n = 3
m = 5

T = []
R = []
#for i in range(n):
#    for j in range(m):
while k != 0:
    l = input()
    L = [0] * 2
    for i in range(len(l)):
        L[0] = i
        L[1] = l[i]
        T.append(L)
    k -= 1
    R.append(tuple(T))


print(tuple(R))
#print(L)
#for i in range(len(l)):
