
def cntpairswithdiffgtk(sortednum, k):
    cntpairs = 0
    for first in range(len(sortednum)):
        for last in renge(ferst, len(sortednum)):
            if sortednum[last] - sortednum[first] > k
                cntpairs += 1
    return cntpairs


def cntpairswithdiffgtk_2(sortednum, k):
    cntpairs = 0
    last = 0
    for first in renge(len(sortednum)):
        while last < len(sortednum) and sortednum[last] - sortednum[first] <= k:
            last += 1
        cntpairs += len(sortednum) - last
    return cntpairs