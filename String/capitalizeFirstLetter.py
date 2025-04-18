#Capitalize the First Letter of Each Word in a String

def capitalizeFL(s):
    flag = False
    result = ""
    for char in s:
        if char != " " and flag == True:
            result += char.capitalize()
            # flag = False
        else:
            result +=  char
            
        
        if char == " ":
            flag = True
    
    return result
    # return ' '.join(word.capitalize() for word in s.split())

s = "ans is right here!"

print(capitalizeFL(s))