# If a number is divisible by 3, it should print "Consultadd". 
# If divisible by 5, print "Python Training". If divisible by both, print "Consultadd - Python Training".

num = int(input())

# for i in range(num):
if num % 3 == 0 and num % 5 == 0:
    print("Consultadd - Python Training")
elif num % 5 == 0:
    print("Python Training")
elif num % 3 == 0:
    print("Consultadd")
else:
    print("Number is not divisible by 3 or 5")
    
# if __name__ == "__main__":
#     num = int(input("Enter a number: "))
   
#     if i % 3 == 0 and i % 5 == 0:
#         print("Consultadd - Python Training")
#     elif i % 5 == 0:
#         print("Python Training")
#     elif i % 3 == 0:
#         print("Consultadd")