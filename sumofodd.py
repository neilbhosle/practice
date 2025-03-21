start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))


def solution(start, end):
    sum = 0
    if end < start:
        return 0
    for i in range(start, end+1):
        if i % 2 != 0:
            sum += i

    print(f"Sum of odd numbers is {sum}")

check = solution(start, end)
# print(check)

