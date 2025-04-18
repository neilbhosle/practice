# Write a Python program to find the common elements between two lists.

def commonElements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = []
    i = 0
    
    while i < len(list1):
        if list1[i] in list2:
            common.append(list1[i])
        i += 1
    
    return common

ans = commonElements()
print(ans)