# Write a Python program to reverse a string.

str = input()
reverse_string = ""

for char in str:
    reverse_string = char + reverse_string
    print(char)
    print(reverse_string)

print(reverse_string)


