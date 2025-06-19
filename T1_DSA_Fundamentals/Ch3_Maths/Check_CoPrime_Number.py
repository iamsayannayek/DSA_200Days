"""
Co-prime: The two numbers, whose have GCD/HCF = 1 means only one common factor should present then it called Co-prime
but more than one common factor is not a Co-prime number
like, 8,15
"""

def findGCD(num1, num2):
    while num1>0 and num2>0:
        if num1>num2:
            num1 = num1%num2
        else:
            num2 = num2%num1
    return num1 if num2==0 else num2

def check_CoPrime(a, b):
    res = findGCD(a, b)
    return True if res==1 else False

c, d = 2, 4

print(check_CoPrime(c, d))

