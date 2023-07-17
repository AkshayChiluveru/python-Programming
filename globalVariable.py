#  In a function, how do you create a global variable?
# We can create a global variable by designating it as global within every function that assigns to it; we can utilize it in other functions:

# Code

# the global keyword is used todeclare that a variable is a global variable and should be accessed from the global scope. 

# global_var = 0  
# def modify_global_var():  
#     global global_var # Setting global_var as a global variable  
#     global_var = 10  
# def printing_global_var():  
#     print(global_var) # There is no need to declare global variable  
# modify_global_var()  
# printing_global_var() # Prints 10


# x= 5
# print(x)

# def hello():
#     x=5
#     print(f"the local of x is {x}")
#     print("Hello Akshay")

# print(f"the global of x is {x}")
# hello()
# print(f"the global value of x is {x}")


x = 10  # global variable

def my_function():
    global x
    x = 4
    y = 5   # Local variable
    print(y)

my_function()
print(x)