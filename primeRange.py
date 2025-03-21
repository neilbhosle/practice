num = int(input("Enter a number: "))
count = 0
for i in range(2, num+1):
    for j in range(2,(num % 2) + 1):
        if i % j == 0:
            count += 1
            break
    if count != 1:
        print(i)

