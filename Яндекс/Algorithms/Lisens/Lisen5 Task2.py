'''N^3'''
def countzerosumranges(nums):
    cntranges = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            rangesum = 0
            for k in range(i, j):
                rangesum += nums[k]
            if rangesum == 0:
                cntranges += 1
    return cntranges


'''N^2'''
def countzerosumranges_2(nums):
    cntranges = 0
    for i in range(len(nums)):
        rangesum = 0
        for j in range(i, len(nums)):
            rangesum += nums[j]
            if rangesum == 0:
                cntranges += 1
    return cntranges

'''N'''

def countprefixsum(nums):
    prefixsumbyvalue = {0 : 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] += 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue

def countzerosumranges_3(prefixsumbyvalue):
    cntranges = 0
    for nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        cntranges += cntsum * (cntsum - 1) // 2
    return cntranges

