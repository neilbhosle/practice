
arr = [1,2,3,4,5,6]

d = 1

newArr = arr[-d:] + arr[:-d]
newArr2 = arr[d:] + arr[:d]
print(arr)
# print(arr[-d:])
# print(arr[:-d])
print(newArr)
# print(newArr[-2])

print(newArr2)
