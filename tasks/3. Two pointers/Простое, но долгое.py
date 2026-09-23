s = "REddeR"

def is_palindrome(s):
    res = ""
    for symbol in s:
        if symbol.isalnum():
            res += symbol.lower()
    return res == res[::-1]

print(is_palindrome(" "))       # True
print(is_palindrome(""))        # True
print(is_palindrome(".,!?"))    # True
print(is_palindrome("0P"))      # False