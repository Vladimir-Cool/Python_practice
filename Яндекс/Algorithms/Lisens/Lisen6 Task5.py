def lbinsearch(l, r, check, chekparams):
    while l < r:
        m = (l + r) // 2
        if check(m, chekparams):
            r = m
        else:
            l = m + 1
    return l

def checkisgt(index, param):
    seq, x = param
    return seq[index] > x

def checkisge(index, param):
    seq, x = param
    return seq[index] >= x

def findefirst(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countx(seq, x):
    indexgt = findefirst(seq, x, checkisgt)
    indexge = findefirst(seq, x, checkisge)
    return indexgt - indexge