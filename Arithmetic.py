#Operators in python
#Arithmetic Operators (+,-,*,/,//,%,**)

num1 = 60
num2 = 30
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(10 % 3)
print(10 ** 3)

#comparision operators (>,<,>=,<=,==,!=)
num1 = 100
num2 = 200
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

#identity operators (is, is not) two operators
num1 = 100
num2 = 100
print(num1 == num2)
print(num1 is num2)

l1 = [11,12,13,14]
l2 = [11,12,13,14]
print(l1 is l2)
print(l1 is not l2)


# Assignment Operators (= , +=,-=,*=,/=)
num1 = 100
num1 = num1 + 5
print(num1)
num1+=5
print(num1)
num1-=5
print(num1)
num1*=5
print(num1)
num1/=5
print(num1)

#bitwise operators (& AND, | OR, ^=>XOR, >> right shift,<< left shift)

#logical operators (and, or, not)
print(10==10 and 20==20)
print (10 == 10 or 10==20)
print(10==20 or 10==20)
print(not(10==10))
print(not(10==12))

#membership operators ( in , not in)
l = [11,12,13,14,15]
print(13 in l)
s = "Akshay is kaali"
print("Akshay" in s)

print(13 not in l)
print("Akshay" not in s)
print(113 not in l)
print("akshay" not in s)