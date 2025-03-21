# patternrttriangleup.py

def seeding(n:int):
    
    i=0
    
    while i<n:
        j=0
        while j<=i:
            print('*',end='')
            j += 1
        i += 1
        print()
    
seeding(3)
