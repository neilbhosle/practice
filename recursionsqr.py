
def poweroftwo(n):
    if n==1:
        return True
    elif n==0 or n%2!=0:
        return False
    else:
        return poweroftwo(n//2)
    
print(poweroftwo(12))