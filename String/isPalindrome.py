def palindrome(s):
    
#     return s == s[::-1]

# s = 'oyo'
# print(palindrome(s))

    left, right = 0, len(s)-1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
    
s = 'amanaplanacanalpanama'
r = 'high'

print(palindrome(s))
print(palindrome(r))

