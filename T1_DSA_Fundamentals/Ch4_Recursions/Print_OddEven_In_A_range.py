def printOddEven(start, end):
    if start>end:
        return
    if start%2 == 0:
        print(f"{start} -> Even")
    else:
        print(f"{start} -> Odd")

    printOddEven(start+1, end)

printOddEven(1, 20)