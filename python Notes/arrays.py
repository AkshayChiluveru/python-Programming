# Arrays are used to store multiple values in one single variable

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.

# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

# The solution is an array!

# An array can hold many values under a single name, and you can access the values by referring to an index number.

# Access the Elements of an Array
# You refer to an array element by referring to the index number.


# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Example
# Get the value of the first array item:

# x = cars[0]
# Example:
# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

# modify the value of the first array item:
cars[0] = 'Toyota'
print(cars)

# return the number of elements in the cars array
print(len(cars))

# print each item in the cars array using loops:

for i in cars:
    print(i)


# Adding Array element
#  Add one more element to the cars array:

cars.append('Maruti')
print(cars)

# Removing an element 
# you can use pop() method to remove an element from the array

cars.pop(1)
print(cars)


# you can also use remove() method to remove the element from the array.

cars.remove('Maruti')
print(cars) 

# sort the list

x1 = [3,6,2,4,7,9,8]
x1.sort()
print(x1)



