def selectionSort(arr, i, j, max=0):
    if i == 0:
        return
    if j<i:
        if arr[j] > arr[max]:
            selectionSort(arr, i, j+1, j)
        else:
            selectionSort(arr, i, j+1, max)
    else:
        arr[max], arr[i-1] = arr[i-1], arr[max]
        selectionSort(arr, i-1, 0, 0)

a = [3, 1, 5, 4, 2]
selectionSort(a, len(a), 0)
print(a)