def sumOf1toN(num):
    if num <= 1:
        return num
    return sumOf1toN(num-1) + num

print(sumOf1toN(2))
