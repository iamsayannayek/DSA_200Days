def reverseNum(num):
    ansNum = 0
    while num != 0:
        digit = num % 10
        ansNum = (ansNum * 10) + digit
        num //= 10
    return ansNum

def checkPalindrome(num):
    revNum = reverseNum(num)
    return True if revNum==num else False

num = 1221
print(checkPalindrome(num))

