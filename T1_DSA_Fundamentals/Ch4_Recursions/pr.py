def binary(num):
    if num == 0:
        return num
    return binary(num//2) * 10 + (num%2)

print(binary(2))