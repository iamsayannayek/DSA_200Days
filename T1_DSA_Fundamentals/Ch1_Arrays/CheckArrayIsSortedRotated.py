#Brute Force
"""
With Every rotation, we check that the array is sorted or not
"""
def bruteForce(arr):
    n = len(arr)
    sortedArr = [0] * n

    for r in range(n+1):
        idx = 0
        # r -> n
        for i in range(r, n):
            sortedArr[idx] = arr[i]
            idx += 1

        # Remaining first values from 0 to r
        for i in range(0, r):
            sortedArr[idx] = arr[i]
            idx += 1

        # Check the sorted array that we get is actually sorted or not
        isSorted = True
        for i in range(n-1):
            if sortedArr[i] > sortedArr[i+1]:
                isSorted = False
        if isSorted:
            return True
    return False

#Better Approach
def betterApproach(arr):
    sortedArr = sorted(arr)
    for r in range(len(arr)):
        isSorted = True
        for i in range(len(arr)):
            if sortedArr[i] != arr[(i+r)%len(arr)]:
                isSorted = False
        if isSorted:
            return True
    return False

# Optimal Approach
"""
In sorted and rotated array we get always a peak value in one or zero not more 
than that but if it's not then it's not a sorted and rotated array
"""
def checkArray(arr):
    peak = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i+1)%len(arr)]:
            peak += 1
    return False if peak>1 else True