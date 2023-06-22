"""what are strings?

In python, anything that you enclose between single or double quotation marks is considered a string. 
A string is essentially a sequence or array of textual data. strings are used when working with unicode characters.

"""
name = "Akshay"
print(" My name is: " + name)


# Sometimes user might need to put quotation marks in between the strings,
# example, consider the sentence: He said, "I want to eat an apple".

print('He said, "I want to eat an apple"')

# Accessing characters of a string
# string is like an array of characters. We can access parts of string by using its index which starts from 0
# Square brackets can be used to access elements of the string.

print(name[0])
print(name[1])
print(name[2])
# print(name[7]) #throws an error

# looping through the string 
# we can loop through strings using a for loop like this:

a = ''' he said,
bring a chair that is 
in the backyard '''

for c in a:
    print(c)



# String Slicing and operations on String:
# Length of a String
# we can find the length of a string using len() function.
# ex:
fruit = "Mango"
len1 = len(fruit)
print("mango is a" ,len1 , "letter word")


# String as an array:
# A string is essentially a sequence of characters also called an array.
# Thus we can access the elements of this way.

fruit1 = "Pineapples"
len2 = len(fruit1)
print(len2)
print(fruit1[0:10])
print(fruit1[4:10])
print(fruit1[:8])
print(fruit1[6:])
print(fruit1[:-3])
print(fruit1[3:-4])
print(fruit1[-6:])
print(fruit1[-2:-7])
print(fruit1[-7:-2])
