# Write a Python program to find the frequency of each element in a list.

def frequency():
    
    li = [23, 56, 43, 12, 67, 98, 14, 90, 23, 12, 98, 67]
    freq = {}
    
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    print(freq)
    
frequency()