def printArray(arr, i=0):
    if len(arr)-1 == i:
        print(arr[i])
        return
    print(arr[i], end=", ")
    printArray(arr, i+1)

nums = [43, 12, 13, 77, 32, 45]
printArray(nums)