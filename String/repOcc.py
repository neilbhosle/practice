def repOcc(old, new, s):
    
    words = s.split()
    # ans = ""
    # for word in words:
    #     if word == old:
    #         ans += new
    #         ans += " "
    #     else:
    #         ans += word
    #         ans += " "
    
    # return ans
    
    new_s = " ".join(["Coding" if word.lower() == "programming" else word for word in words])
    return new_s

s = "I love programming"
print(repOcc("programming","coding",s))
