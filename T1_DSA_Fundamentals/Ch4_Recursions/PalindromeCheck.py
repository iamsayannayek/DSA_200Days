def palindromeCheck(s, start=0, end=None):
    if end == None:
        end = len(s) - 1

    if start>=end:
        return True

    if s[start] != s[end]:
        return False

    return palindromeCheck(s, start+1, end-1)

print(palindromeCheck("ANA"))
