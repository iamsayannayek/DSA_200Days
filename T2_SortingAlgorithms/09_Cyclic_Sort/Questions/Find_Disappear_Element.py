def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        cInd = nums[i] - 1
        if nums[i] != nums[cInd]:
            nums[i], nums[cInd] = nums[cInd], nums[i]
        else:
            i += 1
    ans = []
    for i in range(len(nums)):
        if nums[i] != (i + 1):
            ans.append(i + 1)
    return ans