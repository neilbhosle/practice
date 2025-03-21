li = [1,2,3,6,3,6,3,4,7,8,9,7,8,9,76,3,3,5,89,0,2,4,34,7,2,1]
freq = {}
for i in range(len(li)):
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    
print(freq)
print(type(freq))
