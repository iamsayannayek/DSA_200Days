def factorialNum(n):
    a = 1
    if n==1:
        return a

    for i in range(2, n+1):
        a *= i
    return a

num = 5
print(f"{num}! = {factorialNum(num)}")