def selectionSort(arr):
    for i in range(len(arr)):
        last = len(arr)-i-1 #We take the last index in a manner because every time the element sorts from the last, so no need to sort again again till last
        maxIndex = getMax(arr, 0, last)
        arr[last], arr[maxIndex] = arr[maxIndex], arr[last]


def getMax(arr, start, end):
    max = start
    for i in range(start, end+1): #We go till end+1 because in the last element we also check that, it's max or not
        if arr[max]<arr[i]:
            max = i
    return max

a = [3, 1, 5, 4, 2]
selectionSort(a)
print(a)