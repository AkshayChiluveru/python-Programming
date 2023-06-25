# if else statements:

# Sometimes the programmer needs to check the evaluation of certain expressions, whether the expressions evaluate to true or false . If the expresssion evaluates to false, then the program execution follows a different path than it would have if the expression had evaluated to true.

# based on this, the conditional statements are further classified into following types:

# 1. if
# 2. if-else
# 3. if-else-elif
# 4. nested if-else-elif


# conditional operators:
#  > ,< , >=,<=, ==, !=

a = int(input("Enter your age: ")) 
print("Your age is: ",a)
if a > 18:
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")



num1 = 100
num2 = 200
if num1 > num2:
	print("num1 is greater than num2")
elif num2 > num1:
	print("num2 is greater than num1")
else:
	print("both are equal")



n = int(input("Number: "))
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and 2<=n<=5:
    print("Not Weird")
elif n%2 == 0 and 6<= n <= 20:
    print("Weird")
elif n%2 == 0 and n>20:
    print("Not Weird")
    
