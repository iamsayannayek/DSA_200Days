def applyOperations(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i] * 2
            nums[i + 1] = 0

    nonZeroInd = 0
    for num in nums:
        if num != 0:
            nums[nonZeroInd] = num
            nonZeroInd += 1

    for i in range(nonZeroInd, len(nums)):
        nums[i] = 0

    return nums