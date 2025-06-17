def armstrongNumber(num):
    n = num
    l = len(str(num))
    ans = 0
    while num != 0:
        digit = num % 10
        ans += pow(digit, l)
        num //= 10

    return True if ans == n else False

print(armstrongNumber(1124))