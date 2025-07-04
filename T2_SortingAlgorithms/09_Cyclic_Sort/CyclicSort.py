def cyclicSort(arr):
    i = 0
    while i<len(arr):
        correctIndex = arr[i]-1 # Correct Index = Value - 1; if the elements range within the 1 to N
        if arr[i] != arr[correctIndex]: #Checking the i-th index element is equal to the correct-index element
            arr[correctIndex], arr[i] = arr[i], arr[correctIndex]
        else:
            i += 1

ab = [5, 2, 4, 3, 1]
cyclicSort(ab)
print(ab)

