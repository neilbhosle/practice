lp = int(input("Enter a year: "))

if lp % 400 == 0 and lp %100 == 0:
    print(f"{lp} is leap year")
elif lp % 4 == 0 and lp % 100 != 0:
    print(f"{lp} is leap year")
else:
    print(f"{lp} is not leap year")
