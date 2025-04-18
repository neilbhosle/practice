# Write a Python program to find the sum of all elements in a list.

numStr = input("Enter numbers with a space in between: ")
numList = [int(x) for x in numStr.split()]

total = 0

for num in numList:
    
    total += num
    
print(total)

