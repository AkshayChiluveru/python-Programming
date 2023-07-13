# Python Program to Make a Simple Calculator
# Simple Calculator by Using Functions

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("choose the option ")
print("1. Add")
print("2. Subtract")
print("3. multiply")
print("4. Divide")
    

while True:
    choice = input("Choose the option from the above: ")
    if choice in ('1','2','3','4'):
        num1 = float(input("enter the number 1: "))
        num2 = float(input("enter the number 2: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        break

    else:
        print("Invalid Input")
