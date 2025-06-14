def checkArray(arr):
    peak = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i+1)%len(arr)]:
            peak += 1

    return False if peak>1 else True