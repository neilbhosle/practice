
val = input()
chr = 0
num = 0

for v in val:
    if v.isalpha():
        chr += 1
    elif v.isdigit():
        num += 1

print(f"Number of characters is {chr}, number of digits is {num}")

