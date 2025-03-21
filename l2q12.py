username = 'admin'
password = 'admin'

attempts = 3


while attempts > 0:
    usrnm = input("Please enter username: ")
    psswrd = input("Please enter password: ")

    if username == usrnm:
        if password == psswrd:
            print("Login successful")
            break
        else:
            attempts -= 1
            print(f"Incorrect password, you've got {attempts} attempts")
        
    else: 
        print("Incorrect user name please try again")

if attempts == 0:
    print("You typed password wrong 3 times, your account is locked")


            