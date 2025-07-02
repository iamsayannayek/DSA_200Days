def bubbleSort(arr):
    i = len(arr)-1
    j = 0

    def bubble(arr, i, j):
        if i == 0:
            return

        if j<i:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            bubble(arr, i, j+1) #"""For the Inner loop"""
        else:
            bubble(arr, i-1, 0) #For passing count

    bubble(arr, i, j)
a = [3, 1, 5, 4, 2]
bubbleSort(a)
print(a)