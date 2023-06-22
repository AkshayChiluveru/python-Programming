# def Akshay():         #creating a function => def
#     print("Hello Akshay")

# Akshay()           # calling that function

# def Akshay(fname):
#     print(fname + " Chiluveru")

# Akshay("Akshay")
# Akshay("Naveena")
# Akshay("Swetha")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Akshay", "Chiluveru")


# def my_function(*kids):
#   print("The youngest child is " + kids[0],kids[1])

# my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child1)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# return value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# passing list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# arbitrary keyword argumetns, ** kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")