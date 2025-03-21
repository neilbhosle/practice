#Count the Number of Vowels in a String

def countV(s):
    count = 0
    
    for char in s:
        if char in 'aeiou':
            count += 1
    
    return count

s = 'ambassador'
print(countV(s))