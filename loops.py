#loops
#for loop
#while loop
# for [variable_name] in [iterable datatype]:
# 	statements
# iterable datatypes: strings list tuple set

# l = [11,12,13,14,15]
# sum = 0
# for value in l:
# 	sum = sum + value
# print(sum)

#range(5) 0 1 2 3 4
#range(10,100) 10,11,12,13,14,......,99
#range(10,100,5) 10,15,20,25,30, ....,95
# sum = 0
# for value in range(1,6):
# 	sum = sum + value
# print(sum)


# continue break enumerate 

# for value in range(1,11):
# 	print(value)

# l = [10,20,30,40,50,60]
# key = 50

# for index,value in enumerate(l):
# 	if value == key:
# 		print("element found at index:" ,index)
# 		break
# 	else:
# 	    continue
# else:
#     print("element not found")	

name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k+1)
  
# for k in range(1, 20001):
#   print(k)

  
# for k in range(1, 12, 3):
#   print(k)

# Iterative Statement --> when we want to execute a group of statement multiple times then we will
# use iterative statements.
# In python we are having two types of iterative statement:
# 1.for loop
# 2.while loop
# Requirement of Iterative Statement:
# Suppose i want to write a code that will print hello world 10000 Times. For that we have two
# approaches:
# 1.We can manually write Hello World 10000 Times.
# 2.We can simply use iterative statement and then print hello world 10000 times.
# Note: First approach is not feasible because we need to write hello world 10000 times which decreases
# the code readability and also increases the code length.
# To fullfill such requierement in more easier manner we need to Iterative Statement(loops).


for i in range(10):
    print("Hello World")

# Note: With the help for loop we can easily print hello world 10 Times by writing 2 lines of
# statements. and It is more feasible as it increases the readibility of the code


# For Loops:

# --> if we want to execute a number of statement in some sequence then we should always use for loop.
# Syntax of For loop:
# for i in sequence:
# body/Statement
# i is known as iterator


# Python Program to print each and every Character of the Given String

x="Edyoda Digital University"
for i in x:
    print(i)



# Python Program to print each and every Element of the Given List

x=[10,20,30,40,50]
for i in x:
    print(i)