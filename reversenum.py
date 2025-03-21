num = int(input())
total = 0

while num > 0:
    digit = num % 10
    total = total * 10 + digit
    num //= 10

print(total)
