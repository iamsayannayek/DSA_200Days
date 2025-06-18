"""
Brute Force Approach:
def countZerosFactorial(n):
    a = 1
    for i in range(2, n+1):
        a *= i

    fact = a
    count = 0
    while fact != 0:
        digit = fact % 10
        if digit != 0:
            break
        count += 1
        fact //= 10
    return count

    Here it's not applicable for the higher value, it is exceeded the maximum integer limit in a language
"""
#Optimal Solution
def countTrailingZeros(num):
    res = 0

    i = 5
    while i<=num:
        res = res + (num//i)
        i *= 5
    return res

print(countTrailingZeros(30))

"""
Here we actually calculated the how many 5's are present from 1 to num value. and in num value if there are
5's multiple present then there also a chance that more 5's also present in that value. So our formulae is
res = [num/5] + [num/multiple of 5's] if n>multiple of 5 means
If num = 130
res = [num/5] + [num/25] + [num/125]
"""