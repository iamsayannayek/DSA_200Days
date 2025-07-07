def rearrangeArray(nums):
    pNums = [i for i in nums if i > 0]
    nNums = [i for i in nums if i < 0]

    for i in range(len(pNums)):
        nums[2 * i] = pNums[i]
        nums[2 * i + 1] = nNums[i]

    return nums


