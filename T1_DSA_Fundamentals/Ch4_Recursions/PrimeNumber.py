def checkPrime(num, i=2):
    if num<=1:
        return False

    if num%i == 0:
        return False

    if i*i > num:
        return True

    return checkPrime(num, i+1)

print(checkPrime(101))


