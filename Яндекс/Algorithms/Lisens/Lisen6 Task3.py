def rbinsearch(l, r, check, chekparams):
    while l < r:
        m = (l + r) // 2
        if check(m, chekparams):
            l = m
        else:
            r = m - 1
    return l

def checkstikers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n
