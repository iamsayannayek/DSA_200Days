def large(arr, i=0, max=0):
    if len(arr) == i:
        return max

    if i==0:
        max = arr[i]

    if max < arr[i]:
        max = arr[i]

    return large(arr, i+1, max)

print(large([-11, -22, -5, -111]))

