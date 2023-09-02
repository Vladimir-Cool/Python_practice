import time

def First (A:list, B:list) -> str:
    start_time = time.monotonic()
    N = len(A)
    C = list()
    if len(A) != len(B):
        print('Строки не равны')
    else:
        for i in range(N):
            if B[i] == A[i]:
                A[i] = 0
                B[i] = 0
        for i in range(N):
            for j in range(N):
                if B[i] == 0:
                    break
                elif B[i] == A[j] != 0:
                    A[j] = 1
                    B[i] = 1
                    break
        for k in range(N):
            if B[k] == 0:
                C.insert(k, 'P')
            elif B[k] == 1:
                C.insert(k, 'S')
            else:
                C.insert(k, 'I')
    return (''.join(C), {time.monotonic() - start_time})

def Sekond (A:list, B:list) -> str:
    start_time = time.monotonic()
    N = len(A)
    C = list()
    if len(A) != len(B):
        print('Строки не равны')
    else:
        for i in range(N):
            if B[i] == A[i]:
                A[i] = 0
                B[i] = 0
            for j in range(N):
                if B[i] == 0:
                    break
                elif B[i] == A[j] != 0:
                    A[j] = 1
                    B[i] = 1
                    break
        for k in range(N):
            if B[k] == 0:
                C.insert(k, 'P')
            elif B[k] == 1:
                C.insert(k, 'S')
            else:
                C.insert(k, 'I')
    return (''.join(C), {time.monotonic() - start_time})


#A = list(input())
#B = list(input())
A = ['A', 'B', 'C', 'B', 'C', 'Y', 'A']
B = ['Z', 'B', 'B', 'A', 'C', 'A', 'A']

print(First(A, B))
