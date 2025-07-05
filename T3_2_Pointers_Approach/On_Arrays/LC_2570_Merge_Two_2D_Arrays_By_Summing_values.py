def mergeArrays(arr1, arr2):
    i = j = 0
    ans = []
    while i<len(arr1) and j<len(arr2):
        # When IDs are equal
        if arr1[i][0] == arr2[j][0]:
            ans.append([arr1[i][0], (arr1[i][1] + arr2[j][1])])
            i += 1
            j += 1
        elif arr1[i][0] < arr2[j][0]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i<len(arr1):
        ans.append(arr1[i])
        i += 1

    while j<len(arr2):
        ans.append(arr2[j])
        j += 1
    return ans

num1 = [[1, 2], [2, 3], [4, 5]]
num2 = [[1, 4], [3, 2], [4, 1]]

ans = mergeArrays(num1, num2)
print(ans)