def generateFibonacciNumbers(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a+b
        a = b
        b = c

n = int(input("Enter a limit: "))
generateFibonacciNumbers(n)
