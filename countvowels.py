
str = 'Hello World AEIOU'
count = 0
for i in str:
    if i in 'aeiouAEIOU':
        count += 1

print(count)
