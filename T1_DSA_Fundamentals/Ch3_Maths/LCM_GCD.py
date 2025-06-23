def GCD_LCM(n1, n2):
    gcd = 1
    a = n1
    b = n2

    # while a>0 and b>0:
    #     if a>b:
    #         a = a%b
    #     else:
    #         b = b%a
    #
    # gcd = b if a==0 else a

    #Standard Way to find GCD
    while b!=0:
        a, b = b, a%b

    gcd = a

    lcm = (n1 * n2)//gcd

    return [lcm, gcd]

print(GCD_LCM(12, 14))