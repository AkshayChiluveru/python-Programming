import json

iput1 = input("Enter the number 1 to register , or 2 to login: ")
if iput1 == "1":
    uname = input("Enter the username to register: ")
    password = input("Enter the password: ")

    reg = {
        "username":uname,
        "password":password
    }

    with open("practice/login.json", "w") as f:
        json.dump(reg, f,indent = 2)

elif iput1 == "2":
    uname = input("Enter the username to login: ") 
    pwd = input("Enter the password to login: ")

    reg = {
        "username":uname,
        "password": pwd
    }
    with open("practice/login.json", "r") as f:
        json.load(reg,f, indent = 2)




else:
    print("you must choose 1 or 2")

