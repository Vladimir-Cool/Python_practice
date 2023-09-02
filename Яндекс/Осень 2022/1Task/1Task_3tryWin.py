

'''Третьий вариант работает оч быстро, Ура'''

def third(A:list, B:list) -> str:
    D = dict()
    for i in range(len(B)):
        if A[i] == B[i]:
            B[i] = 0
            A[i] = 0
        else:
            if A[i] not in D:
                D[A[i]] = 0
            D[A[i]] += 1
    C = [0] * len(B)
    for j in range(len(B)):
        if B[j] == 0:
            C[j] = 'P'
        elif B[j] in D:
            if D[B[j]] > 0:
                C[j] = 'S'
                D[B[j]] -= 1
            else:
                C[j] = 'I'
        else:
            C[j] = 'I'
    return (''.join(C))


#A = list(input())
#B = list(input())
A = ['A', 'B', 'C', 'B', 'C', 'Y', 'A']
B = ['Z', 'B', 'B', 'A', 'C', 'A', 'A']

print(third(A, B))