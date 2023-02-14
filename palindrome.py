def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

s = "LOL"
result = is_palindrome(s)
print(result)
