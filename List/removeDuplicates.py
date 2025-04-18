 # Write a Python program to remove duplicates from a list.
 
# def removeDuplicate():
    # li = [23, 56, 43, 12, 67, 98, 14, 90, 43]
    
#     seen = {}
#     duplicate = 0
    
#     for i in li:
#         duplicate = i
#         if i in seen:
#             li.remove(i)
#         else:
#             seen.append(i)

#     print(duplicate)
    
#     return li

# removeDuplicate()

def remove_duplicates():
    lst = [23, 56, 43, 12, 67, 98, 14, 90, 43]
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    print(result)
    return result

remove_duplicates()

