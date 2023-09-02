'''Первый вариант'''
def interstations(N, i, j):
    if j > i:
        rigth = j - i - 1
        left = N - j +i - 1
        return min(rigth, left)
    else:
        rigth = N - i + j - 1
        left = i - j - 1
        return min(rigth, left)


'''Вариант с модулем'''
def interstations_2(N, i, j):
    dist1 = abs(j - i) - 1
    dist2 = N - 2 - dist1
    return min(dist1, dist2)

N, i, j = map(int, input().split())

print(interstations(N, i, j))
print(interstations_2(N, i, j))

