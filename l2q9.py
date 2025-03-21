# Write a Python program that executes an operation on a list and handles an IndexError exception 
# if the index is out of range.

def indexHandling(idx,ls):
    try:
        return ls[idx]
    except IndexError:
        return "Index out of range"
    

ls = [1,2,3,4,5,6]
idx = int(input("enter an Index "))

print(indexHandling(idx,ls))


