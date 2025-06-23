def FiboSeries(limit):
    def fibo(n):
        if n < 2:
            return n
        return fibo(n - 1) + fibo(n - 2)

    for i in range(limit+1):
        print(fibo(i), end=" ")

FiboSeries(50)

def fiboCal(n):
    if n < 2:
        return n
    return fiboCal(n - 1) + fiboCal(n - 2)

print(fiboCal(50))