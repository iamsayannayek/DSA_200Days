def insertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, 0, -1):
            if arr[j-1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

ar = [5, 3, 4, 1, 2]
insertionSort(ar)
print(ar)