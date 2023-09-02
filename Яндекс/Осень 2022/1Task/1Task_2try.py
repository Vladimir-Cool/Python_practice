import time

def Sekond(A:list, B:list) -> str:
    start_time = time.monotonic()
    C = list()
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i] == A[i]:
                C.append('P')
                A[i] = 0
                break
            elif B[i] == A[j] and B[j] != A[j]:
                C.append('S')
                A[j] = 0
                break
            elif j == len(A)-1:
                C.append('I')
    return(''.join(C), {time.monotonic() - start_time})




#A = list(input())
#B = list(input())
A = ['A', 'B', 'C', 'B', 'C', 'Y', 'A'] * 1000
B = ['Z', 'B', 'B', 'A', 'C', 'A', 'A'] * 1000

print(Sekond(A, B))

