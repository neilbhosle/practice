num = int(input("Enter a number: "))
count = 0

if num == 1:
    print("1 is not prime")
    
for i in range(2,(num // 2) + 1):
    if num % i == 0:
        count += 1
    
    if count == 1:
        break

if count == 1:    
    print("Not Prime number")
else:
    print("Prime number")