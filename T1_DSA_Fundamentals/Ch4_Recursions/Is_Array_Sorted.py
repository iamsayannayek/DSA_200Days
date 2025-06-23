def isSorted(arr, i=0):
    if len(arr)-1 == i:
        return True

    if arr[i]>arr[i+1]:
        return False

    return isSorted(arr, i+1)

print(isSorted([7, 1, 2, 3, 4, 5]))

