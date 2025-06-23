def reverseAString(s, i=0, ans=""):
    if i == len(s):
        return ans
    ans += s[len(s)-i-1]
    return reverseAString(s, i+1, ans)

print(reverseAString("123456789"))
