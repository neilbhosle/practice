
arr = [6,3,4,8,2,9,0,1]

for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            
    
print(arr)