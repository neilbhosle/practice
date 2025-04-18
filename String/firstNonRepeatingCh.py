#Find the First Non-Repeating Character in a String
from collections import defaultdict
def firstNRC(s):
    count = defaultdict(int)
    
    dic = {}
    
    
    for char in s:
      if char.isalnum():
        if char in dic:
            return char
        dic[char] = 1
      
        
    for char in s:
        if count[char] == 1:
            return f"First non repeating character is {char}"
        
        
    

s = "Im a software developer"

print(firstNRC(s))
