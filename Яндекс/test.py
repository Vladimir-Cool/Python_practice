

def finalist(S:list, K:int) -> list:
    final = []
    j = 0
    while j < K:
        i = 0
        while i < len(S) - 1 - j:
            if S[i][0] > S[i+1][0]:
                S[i], S[i+1] = S[i+1], S[i]
            elif S[i][0] == S[i+1][0]:
                if S[i][1] < S[i+1][1]:
                    S[i], S[i+1] = S[i+1], S[i]
            i += 1
        final.append(S[-j - 1][2])
        j += 1
    return final

S = [ (11, 20, 'Bob'), (11, 100, 'cheburashka'), (10, 0, 'dambo'), (2, 30, 'Ms_Potato'), (10, 20, 'Robert')]
K = 4
print(finalist(S, K))


