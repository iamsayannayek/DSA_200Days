def firstMissingPositive(arr):
    i = 0
    while i < len(arr):
        cId = arr[i] - 1
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[cId]:
            arr[i], arr[cId] = arr[cId], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1

    return len(arr) + 1