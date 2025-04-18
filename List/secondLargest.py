# Second largest number in a list

def secondLargest():
    li = [23, 56, 43, 12, 67, 98, 14, 90]
    first, second = li[0], li[0]
    for num in li:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    
    return second

ans = secondLargest()
print(ans)