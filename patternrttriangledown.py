def seeding(n: int) -> None:
    i = n
    while i > 0:
        j = 0  
        while j < i:
            print('*', end='')
            j += 1
        i -= 1
        print()


seeding(3)
