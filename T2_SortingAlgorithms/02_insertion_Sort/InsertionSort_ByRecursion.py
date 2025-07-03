def insertionSort(arr, n, i=0):
    if i == n-1:
        return
    j = i+1
    while j>0 and arr[j-1]>arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
    insertionSort(arr, n, i+1)

ar = [5, 3, 4, 1, 2]
insertionSort(ar, len(ar))
print(ar)
