def setMismatch(nums):
    i = 0
    n = len(nums)
    while i < n:
        cInd = nums[i] - 1
        if nums[i] != nums[cInd]:
            nums[i], nums[cInd] = nums[cInd], nums[i]
        else:
            i += 1

    ans = []

    for i in range(n):
        if nums[i] != i + 1:
            ans.append(nums[i])  # Repeating Number present at wrong Index
            ans.append(i + 1)  # Missing Number that not present
    return ans