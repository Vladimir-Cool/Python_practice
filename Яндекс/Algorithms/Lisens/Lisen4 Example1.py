
def countsort (seq:list) -> list:
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval +1)
    count = [0] * k
    for now in seq:
        count[now - minval] += 1
    nowpos = 0
    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
