def bubbleSort(arr):
    """For counting the passes"""
    for i in range(0, len(arr)):
        swapped = False
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swapped = True
        if not swapped:
            break

a = [3, 1, 5, 4, 2]
bubbleSort(a)
print(a)

