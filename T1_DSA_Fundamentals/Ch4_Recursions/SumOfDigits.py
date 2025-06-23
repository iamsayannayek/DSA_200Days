def sumOfDigits(num):
    if num == 0:
        return num
    return sumOfDigits(num//10) + (num%10)

print(sumOfDigits(123456789))
