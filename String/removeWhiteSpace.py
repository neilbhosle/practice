#Remove All Whitespace from a String

def removeWS(s):
    
    # ans = s.replace(" ","")
    
    # return ans
    ans = ""
    for char in s:
        if char != " ":
            ans += char
    return ans

s = "I'm a software developer"

print(removeWS(s))

