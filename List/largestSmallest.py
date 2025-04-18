# Write a Python program to find the largest and smallest number in a list.

def largeSmall():
    li = [23, 56, 43, 12, 67, 98, 14, 90]
    
    if not li:  # Handle empty list
        return None, None
    
    largest = smallest = li[0]  # Initialize with first element
    
    for num in li:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    print(f"Largest: {largest}, Smallest: {smallest}")

largeSmall()
