marks = [100,98,99,97,87]
total_marks = 0

for i in marks:
    total_marks += i

percent = total_marks / 5

if percent >= 90:
    print("A Grade")
elif percent >= 80:
    print("B Grade")
elif percent >= 70:
    print("C Grade")
elif percent >= 60:
    print("D Grade")
elif percent >= 40:
    print("E Grade")
else: 
    print("F Grade")
    
