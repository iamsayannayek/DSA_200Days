def findDuplicate(nums):
     for i in range(len(nums)):
         num = abs(nums[i])
         idx = num - 1

         if nums[idx] < 0:
            return num
         else:
             nums[idx] *= (-1)


"""------------- By Cyclic Sort ----------------"""
def findDuplicate_By_CyclicSort(nums):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] != i + 1:
            cInd = nums[i] - 1
            if nums[i] != nums[cInd]:
                nums[i], nums[cInd] = nums[cInd], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return -1

