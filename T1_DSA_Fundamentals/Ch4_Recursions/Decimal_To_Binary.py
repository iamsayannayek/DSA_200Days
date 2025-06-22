def binary(num):
    if num == 0:
        return ""
    return binary(num//2) + str(num % 2)

# To handle input 0
def decimalToBinary(num):
    if num == 0:
        return "0"
    return binary(num)

print(decimalToBinary(13))