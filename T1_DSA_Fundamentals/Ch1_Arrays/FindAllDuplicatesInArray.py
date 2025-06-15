def findDuplicate(arr):
    ans = []
    for i in range(len(arr)):
        num = abs(arr[i])
        idx = num - 1

        if arr[idx] < 0:
            ans.append(num)
        else:
            arr[idx] *= -1

    return ans

nums = [4, 3, 2, 7, 8, 2, 3, 1]
#Output: [2, 3]
print(findDuplicate(nums))