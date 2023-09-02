def lbinsearch(l, r, check, chekparams):
    l = 0
    r = N
    while l < r:
        m = (l + r) // 2
        if check(m, chekparams):
            r = m
        else:
            l = m + 1
    return l

def checkendownment(m, params):
    n, k = params
    return (k + m) * 3 >= n + m


