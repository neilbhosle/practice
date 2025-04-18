# Merge two lists into a single sorted list

def mergeLists():
    list1 = [3, 1, 4, 1, 5]
    list2 = [9, 2, 6, 5, 3]
    merged = []
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

ans = mergeLists()

# def merge_sorted_lists(list1, list2):
#     list1 = sorted(list1)
#     list2 = sorted(list2)
#     merged = []
#     i = j = 0
    
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
    
#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
#     return merged

# list1 = [3, 1, 4, 1, 5]
# list2 = [9, 2, 6, 5, 3]
# ans = merge_sorted_lists(list1, list2)

print(ans)

        
        