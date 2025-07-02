import math


def fibonacciNum(n):
    # return int((1 / math.sqrt(5)) * (((((1 + math.sqrt(5))/2)**n)) - (((1 - math.sqrt(5))/2)**n)))
    return int((((((1 + math.sqrt(5))/2)**n)) - (((1 - math.sqrt(5))/2)**n))// math.sqrt(5))

for i in range(10):
    print(fibonacciNum(i), end=", ")

# print(fibonacciNum(50))