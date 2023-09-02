
def twotermswithsumx(nums, x):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == x:
                return nums[i], nums[j]
    return 0, 0

def twotermswithsumx2(nums, x):
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0

nums = [2, 4, 6]
x = 6
print(twotermswithsumx(nums, x))
print(twotermswithsumx2(nums, x))