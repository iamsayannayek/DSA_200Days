def bSearch(arr, target, start, end):
    if start>end:
        return -1
    mid = start + (end-start)//2

    if arr[mid] == target:
        return mid

    if target < arr[mid]: #If Target is on the left side of the array
        return bSearch(arr, target, start, mid-1)
    # If Target is on the Right side of the array
    return bSearch(arr, target, start+1, end)

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    return bSearch(arr, target, start, end)

nums = [12, 23, 43, 54, 62, 76, 82, 87, 99, 100]
print(binarySearch(nums, 5))