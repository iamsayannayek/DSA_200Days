"""
Note:
    ASCII Values for:
        Capital Letters: 65 -> 90
        Small Letters: 97 -> 122
        Digits: 48 -> 57
        Specials: Others Values
"""
s = "gvdvgfvv33268yb83y2b#W^62b828n98nmB@&7b-309=m04=undhgswagwt672!@78yn2ywb9n!b`8~) 21-MWT^%@V!0[- mGHTQBV!%!n"
# Without built-in method:
def withOutBuiltIn(s):
    letters = digits = special = 0
    for char in s:
        ASCII = ord(char)
        #For Uppercase and Lowercase letters
        if (65<=ASCII<=90) or (97<=ASCII<=122):
            letters += 1
        # For Digits
        elif 48<=ASCII<=57:
            digits += 1
        else:
            special += 1

    return [letters, digits, special]

# With built-in Method:
def withBuiltIn(s):
    letters = digits = special = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
