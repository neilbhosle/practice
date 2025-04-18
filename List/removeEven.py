# Write a Python program to remove all even numbers from a list.

def removeEven():
    
    list1 = [1, 2, 3, 4, 5]
    
    for i in list1:
        if i % 2 == 0:
            list1.remove(i)
            
    
    return list1

ans = removeEven()
print(ans)