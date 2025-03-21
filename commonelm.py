
# list1 = int(input('List 1: '))
# list2 = int(input('List 2: '))

# common = [num for num in list1 if num in list2 ]

# print(common)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = [x for x in list1 if x in list2]

print(common_elements) 

cmn_lem = list[set(list1) & set(list2)]

print(cmn_lem)