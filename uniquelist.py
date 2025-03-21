
def uniquelm(li):
    unique = list(set(li))
    return unique

li = [1,1,2,2,3,4,5,6,6,7,6,8,7,9]

ans = uniquelm(li)

print(ans)

def unique_elements(input_list):
    return list(set(input_list))

list1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(f"Unique elements: {unique_elements(list1)}")