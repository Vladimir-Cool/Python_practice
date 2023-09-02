
def combinations(n:int, k:int):
    if k > n or n < 0 or k < 0:
        return 0
    elif k == n:
        return 1
    else:
        return combinations(n - 1, k) + combinations(n - 1, k - 1)


n, k = map(int, input().split())
print(combinations(n, k))
