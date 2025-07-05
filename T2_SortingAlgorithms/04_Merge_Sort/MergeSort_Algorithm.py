def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(firstArr, secondArr):
    mixArr = []
    i = j = 0

    while i < len(firstArr) and j < len(secondArr):
        if firstArr[i] <= secondArr[j]:
            mixArr.append(firstArr[i])
            i += 1
        else:
            mixArr.append(secondArr[j])  # ✅ fix: add secondArr[j], not secondArr
            j += 1

    # Add remaining elements from firstArr
    while i < len(firstArr):
        mixArr.append(firstArr[i])
        i += 1

    # Add remaining elements from secondArr
    while j < len(secondArr):
        mixArr.append(secondArr[j])
        j += 1

    return mixArr

# Example usage
ar = [3, 4, 2, 1, 7, 9, 3]
meAr = mergeSort(ar)
print(f"{ar} After Sorting -> {meAr}")
