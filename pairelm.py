arr = [1,2,3,4,5,6]
k = 6

count = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        print(i, j)
        if arr[i] + arr[j] == k:
            count += 1

print('Count ',count)

    