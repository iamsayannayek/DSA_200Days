def pivotArrayBy3Pointers(nums, pivot):
    countLess = equal = 0
    for i in range(len(nums)):
        if nums[i] < pivot:
            countLess += 1
        elif nums[i] == pivot:
            equal += 1

    i = 0
    j = countLess
    k = countLess + equal
    res = [0]*len(nums)
    for l in range(len(nums)):
        if nums[l]<pivot:
            res[i] = nums[l]
            i += 1
        elif nums[l] == pivot:
            res[j] = nums[l]
            j += 1
        else:
            res[k] = nums[l]
            k += 1

    return res

def pivotArrayBy2Pointers(arr, pivot):
    res = [0] * len(arr)
    left = 0
    right = len(arr) - 1

    # First pass: place < pivot at left, > pivot at right
    for num in arr:
        if num < pivot:
            res[left] = num
            left += 1
        elif num > pivot:
            res[right] = num
            right -= 1

    # Second pass: fill pivot values in between
    for i in range(left, right + 1):
        res[i] = pivot

    return res



nums = [9, 12, 5, 10, 14, 3, 10]

print(pivotArrayBy2Pointers(nums, 10))

