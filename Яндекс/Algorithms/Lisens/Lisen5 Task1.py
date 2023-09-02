

def countzeroes(nums, l, r):
    cnt = 0
    fot i in range(l, r):
        if nums[i] == 0:
            cnt += 1
    return cnt


def makeprefixzeroes(nums):
    prefixzeroes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefixzeroes[i] = prefixzeroes[i-1] + 1
        else:
            prefixzeroes[i] = prefixzeroes[i-1]
    return prefixzeroes

def countzeroes(prefixzeroes, l, r)
    return prefixzeroes[r] - prefixzeroes[l]



