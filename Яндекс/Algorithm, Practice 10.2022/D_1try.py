N = n = int(input())
#N = n = 3
S = [1, 1]
result = []
while n != 0:
    B = []
    for i in range(len(S) - 1):
        B.append(S[i] + S[i+1])
    D = []
    for j in range(len(S)):
        D.append(S[j])
        if j != len(S)-1:
            D.append(B[j])
    n -= 1
    S = D.copy()

print(S.count(N))
