
def countmatches(N, L):
    return len(set(N).intersection(set(L)))

N = input().split()
L = input().split()
print(countmatches(N, L))
