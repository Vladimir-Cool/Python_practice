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

def sheckproblemcount(days, param):
    n, k = param
    return (k + (k + days - 1)) * days // 2 >= n
