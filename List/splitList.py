import random

# Write a Python program to split a list into two lists, one for even numbers and one for odd numbers.

numbers = [random.randint(1, 100) for _ in range(10)]
print("Generated list:", numbers)

def splitList(numbers):
    
    # list1 = []
    # list2 = []
    
    # for num in numbers:
    #     if num % 2 == 0:
    #         list1.append(num)
    #     else:
    #         list2.append(num)
            
    # print(f"Even List : ", list1)
    # print(f"Odd List", list2)
    
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    
    print("Even :", even)
    print("Odd :", odd)
    

splitList(numbers)
