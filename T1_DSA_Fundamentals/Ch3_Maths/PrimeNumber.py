"""
Prime Number: When a number has exactly two divisors, then it's called a Prime number. The divisors are 1 and itself.
Example: 2, 5, 13, 17, 11
But here 1 is not prime because it's only having one divisor.
"""

# Brute Force
def bruteForce(n):
    count = 0
    for i in range(n+1):
        if n%i == 0:
            count += 1
    return False if count>2 else True
# But it's taking a lots of Time

"""
Optimal Approach:
Here we not go checking till n but instead of this we go to till sqrt(n) because if in between any number divisible
then the other half also divisible the number.
n = 36
sqrt(36) =6
1 X 36
2 X 18
3 X 12
4 X 9
6 X 6
so we can see if a number divisible by one number then other number means 3 divisible 36,
like 36%3 = 0, we get one divisors again if we check the 36/3 = 12, it's also a divisor of 36 then we count in that time. 
"""
def checkPrime(num):
    count = 0
    i = 1
    while i*i <= num:
        if num%i == 0:
            count += 1
            if num//i != i:
                count += 1
        if count>2:
            break
    return False if count>2 else True