nums = int(input())

# while nums > 9:
#     nums = sum(int(num) for num in str(nums))
#     print(nums)

# print(nums)


        
def sumDigits(num):
    sumDigit = 0
    
    if num < 10:
        return num
    
    while num > 0:
        sumDigit += num % 10
        num //= 10

    return sumDigits(sumDigit)        

print(sumDigits(nums))
