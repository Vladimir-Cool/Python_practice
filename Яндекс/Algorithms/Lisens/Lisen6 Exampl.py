def lbinsearch(l, r, check, chekparams):
    while l < r:
        m = (l + r) // 2
        if check(m, chekparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, chekparams):
    while l < r:
        m = (l + r) // 2
        if check(m, chekparams):
            l = m
        else:
            r = m - 1
    return l