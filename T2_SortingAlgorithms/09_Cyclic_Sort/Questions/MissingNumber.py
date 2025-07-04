def missingNumber(self, arr: List[int]) -> int:
    i = 0
    while i < len(arr):
        correctIndex = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correctIndex]:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if i != arr[i]:
            return i
    return len(arr)