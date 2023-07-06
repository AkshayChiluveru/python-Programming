import sys
from admin_panel import *

admin = Admin_panel()

while True:
    print("Enter 1 for admin login")
    print("Enter 2 for student login")
    print("Enter 3 for trainer login")
    print("Enter 4 for logout")
    print("-"*100)
    choice = int(input("Enter your choice for login: "))
    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        temp = admin.admin_login(username, password)
        if temp:
            print("-"*100)
            print("Enter 1 for add module")
            print("Enter 2 for add trainer")
            print("Enter 3 for add batch")
            print("Enter 4 for add Student")
            print("Enter 5 for remove module")
            print("Enter 6 for upadate module")
            print("Enter 7 for get module details")
            print("Enter 8 for get trainer details")
            print("Enter 9 for get student details")
            print("Enter 10 for get batch details")
            print("-"*100)
            option = int(input("Enter your choice: "))
            print("-"*100)
            if option == 1:
                modulename = input("Enter your module name which you want to add: ")
                duration = input("Enter the duration of the module")
                admin.add_module(modulename,duration)
                print("Module added successfully")
                print("-"*100)
            elif option == 2:
                admin.addTrainer()
                print("Trainer added successfully")
                print("-"*100)
            elif option == 3:
                module = input("Enter your module name which you want to add: ")
                trainer = input("Enter your trainer: ")
                student = input("Enter your student: ")
                admin.add_batch(module,trainer,student)
                print("Batch added successfully")
                print("-"*100)
            elif option == 4:
                admin.add_student()
                print("student added successfully")
                print("-"*100)
            elif option == 5:
                admin.update_module()
                print("Module updated successfully")
                print("-"*100)
            elif option == 6:
                admin.remove_module()
                print("Module removed successfully")
                print("-"*100)
            elif option == 7:
                admin.read_module()
                print("Module read successfully")
                print("-"*100)            
            elif option == 8:
                admin.read_trainer()
                print("trainer read successfully")
                print("-"*100)
            elif option == 9:
                admin.read_student()
                print("Student read successfully")
                print("-"*100)
            elif option == 10:
                admin.read_batch()
                print("batch read successfully")
                print("-"*100)
            else:
                print("Enter a valid input")
                print("-"*100)
        else:
            print("Enter correct username and password")

    elif choice == 2:
        print("-"*100)
        print("Enter 1 for get student details")
        print("Enter 2 for module details")
        print("Enter 3 for get batch details")
        print("-"*100)
        option = input("Enter your chouce: ")
        print("-"*100)
        if option == 1:
            admin.read_module()
            print("-"*100)
        elif option == 2:
            admin.read_student()
            print("-"*100)
        elif option == 3:
            admin.read_batch()
            print("-"*100)
        else:
            print("Enter a valid input")
            print("-"*100)
    

    elif choice == 3:
        print("-"*100)
        print("Enter 1 for get module")
        print("Enter 2 for get trainer")
        print("Enter 3 for get student")
        print("Enter 4 for get batch")
        print("-"*100)
        option = input("Enter your chouce: ")
        print("-"*100)
        if option == 1:
            admin.read_module()
            print("-"*100)
        elif option == 3:
            admin.read_trainer()
            print("-"*100)
        elif option == 3:
            admin.read_student()
            print("-"*100)
        elif option == 4:
            admin.read_batch()
            print("-"*100)
        else:
            print("Enter a valid input")
    
    elif choice == 4:
        print("Thank you for visiting")
        sys.exit()
    
    else:
        print("Please enter a valid input")