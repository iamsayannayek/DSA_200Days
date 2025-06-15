def swapCase(s):
    result = ""
    for char in s:
        ASCII = ord(char)
        # Uppercase to Lowercase
        if 65<=ASCII<=90:
            result += chr(ASCII+32)
        # Lowercase to Uppercase
        elif 97<=ASCII<=122:
            result += chr(ASCII-32)
        else:
            result += char
    return result

"""
There is also a built in function which is .lower() & .upper()
"""