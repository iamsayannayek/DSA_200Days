def findDuplicates(arr):
    i = 0
    while i < len(arr):
        correctIndex = arr[i] - 1
        if arr[i] != arr[correctIndex]:
            arr[correctIndex], arr[i] = arr[i], arr[correctIndex]
        else:
            i += 1

    ans = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            ans.append(arr[i])

    return ans