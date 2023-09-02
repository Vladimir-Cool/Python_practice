def dist(t, param):
    x, v = param
    minpos = maxpos = x[0] + v[0] * t
    for i in range(1, len(x)):
        nowpos = x[i] + v[i] * t
        minpos = min(minpos, nowpos)
        maxpos = max(minpos, nowpos)
    return maxpos - minpos


def checkasc(t, eps, param):
    return dist(t + eps, param) >= disp(t, param)


def fbinsearch(l: int, r: int, eps: int, check, param: list) -> int:
    while l + eps < r:
    m = (l + r) / 2
        if checkasc(m, eps, param):
            r = m
        else:
            l = m
    return l

