def merge1(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    idx = (m + n) - 1
    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[idx] = nums1[i]
            i-=1
        else :
            nums1[idx] = nums2[j]
            j-=1
        idx -=1

"""My code sample"""
def merge2(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    idx = (m + n) - 1

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
            idx -= 1
        else:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1

    while j >= 0:
        nums1[idx] = nums2[j]
        j -= 1
        idx -= 1
