def countDigits(num, count = 0):
    if num == 0:
        return count
    return countDigits(num//10, count+1)

print(countDigits(12345678910))
