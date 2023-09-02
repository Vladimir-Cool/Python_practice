
def merge(nums1:list, nums2:list) ->list:
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    inf = max(nums1[-1], nums2[1]) + 1
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1) + len(nums2) - 2):
        if nums1[first1] <= nums2[first2]:
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    nums1.pop()
    nums2.pop()
    return merged


def merge_2(nums1:list, nums2:list) ->list:
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] <= nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    return merged

