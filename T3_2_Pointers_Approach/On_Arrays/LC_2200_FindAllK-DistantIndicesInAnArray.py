def findKDistantIndices(nums, key, k):
    res = []

    end = 0

    for j in range(len(nums)):
        if nums[j] == key:
            start = max(j-k, end)
            end = min(j+k+1, len(nums))

            while start < end:
                res.append(start)
                start += 1

    return res


print(findKDistantIndices([1,1,2,2,2], 2, 1))