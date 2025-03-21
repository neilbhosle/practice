
# def separateList(strlst):
    
#     result = []
#     for str in strlst:
#         charLst = []
#         for s in str:
#             charLst.append(s)
#         result.append(charLst)
    
#     return result

# res = separateList(['Red','Blue','Green'])
# print(res)
            
li = ['Red', 'Blue', 'Green']

ans = list(map(list,li))

print(ans)