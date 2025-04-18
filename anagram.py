from collections import defaultdict


def anagram():    
    str1 = input()
    str2 = input()

    # if sorted(str1) == sorted(str2):
    #     print("Anagram")
    # else:
    #     print("not Anagram")
    ans = defaultdict(int)
        
    if len(str1) != len(str2):
        return False
    
    for i in str1:
        ans[i] += 1
        
    for i in str2:
        ans[i] -= 1
    
    return all(value == 0 for value in ans.values())

print(anagram())
        