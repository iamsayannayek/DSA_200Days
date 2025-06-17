def reverseNum(num):
    ansNum = 0
    while num != 0:
        digit = num % 10
        ansNum = (ansNum * 10) + digit
        num //= 10
    return ansNum

print(reverseNum(12345))

