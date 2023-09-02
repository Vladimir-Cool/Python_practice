
'''Вычисление процента за месяц'''
def checkmonthlyperc(mperc, ymerc):
    msum = 1 + mperc / 100
    ysum = 1 + ymerc / 100
    return msum ** 12 >= ysum

def fbinsearch(l:int, r:int, eps:int, check, checkparam:int) ->int:
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparam):
            r = m
        else:
            l = m
    return l
x = 8.2
eps = 0.0001
#print(fbinsearch(0, x, eps, checkmonthlyperc, x))
mperc = fbinsearch(0, x, eps, checkmonthlyperc, x)

'''Вычисление процента за месяц'''
def checkcredit(mpay, params):
    period, creditsum, mperc = params
    for i in range(period):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return creditsum <= 0

def fbinsearch_2(l, r, eps, check, checkparam):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparam):
            r = m
        else:
            l = m
    return l

epss = 0.01
m = 2700000
n = 15 * 12

Monthlypay = fbinsearch_2(0, m, epss, checkcredit, (n, m, mperc))
print(Monthlypay)

