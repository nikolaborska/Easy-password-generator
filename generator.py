import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while 1:
    password_len = int(input("How long should your password be: "))
    password_count = int(input("How many passwords you want: "))
   
    pass_list = []

    for x in range (0, password_count):
        password = ""
        for x in range (0, password_len):
            password_char = random.choice(char)
            password = password + password_char
        pass_list.append(password)

    print("This is your password: ")
    for pass1 in pass_list:
        print(pass1)



