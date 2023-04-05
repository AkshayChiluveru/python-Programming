#int
num1 = 100
print(type(num1))

#float
num2 = 12.34
print(type(num2))

s = "new 'to' python"
print(s,type(s))
print(id(s))

#list
#lists are mutable

l = [11,12,13,14,15]
print(l)

l = [11,12,13,14,15, "Akshay","Tinku"]
print(l)
print(id(l))
l.append(60)
print(l)
print(id(l))

#tuple
#tuples are immutable that means once we defined, cannot change tuple
t = (11,12,13,14)

#Dict =>key and value pair
d = {"name": "Akshay","email" : "Akshay@gmail.com"}

#set
s = {10,11,12,13}

#bool => True or False

#complex : 4 + 3j