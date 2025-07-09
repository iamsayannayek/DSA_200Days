def rotate(nums, k):
    def rev(arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    k = k % len(nums)
    rev(nums, 0, len(nums) - 1)
    rev(nums, 0, k - 1)
    rev(nums, k, len(nums) - 1)
