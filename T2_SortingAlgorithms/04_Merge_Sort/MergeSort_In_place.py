def mergeSort(arr, start, end):
    if (end - start) == 1:
        return

    mid = (start + end) // 2

    # Sort the left part
    mergeSort(arr, start, mid)

    # Sort the Right part
    mergeSort(arr, mid, end)

    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    mix = []
    i = start
    j = mid

    while (i < mid) and (j < end):
        if arr[i] < arr[j]:
            mix.append(arr[i])
            i += 1
        else:
            mix.append(arr[j])
            j += 1

    # Remaining element restoration
    while i < mid:
        mix.append(arr[i])
        i += 1

    while j < end:
        mix.append(arr[j])
        j += 1

    # Replace the mix array value to the original vales
    for l in range(len(mix)):
        arr[start + l] = mix[l]

ar = [3, 4, 1, 2]
mergeSort(ar, 0, len(ar))
print(ar)