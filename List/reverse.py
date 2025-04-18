# Write a Python program to reverse a list.

# def reverse():
#     li = [23, 56, 43, 12, 67, 98, 14, 90]
#     end = len(li) - 1
#     temp = 0
#     for num in range(len(li)//2):
#         temp = li[num]
#         li[num] = li[end]
#         li[end] = temp
#         end -= 1
    
#     return li

# ans = reverse()
# print(ans)

def reverse():
    li = [23, 56, 43, 12, 67, 98, 14, 90]
    end = len(li) - 1
    for num in range(len(li)//2):
        li[num], li[end] = li[end], li[num]  
        end -= 1
    return li