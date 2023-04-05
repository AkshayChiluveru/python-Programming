#conditional Operators
# if [condition]:
# 	statements
# elif [condition]:
# 	ststements
# else:
# 	ststements

# num1 = 100
# num2 = 200
# if num1 > num2:
# 	print("num1 is greater than num2")
# elif num2 > num1:
# 	print("num2 is greater than num1")
# else:
# 	print("both are equal")

# 	n1 = 5
# 	n2 = 10
# 	if num1 > num2:
# 		print("n1 is greater than n2")
# 	elif n2 > n1:
# 		print("n2 is greater than n1")
# 	else:
# 		print("Both are equal")

# number1 = 5
# number2 = 5
# if number1 > number2:
# 	print("number1 is greater than number2")
# elif number2 > number1:
# 	print("number2 is greater than number1")
# else:
# 	print("Both are equal")
# print(type({})) 
# ctrl + b to run
# p = float(input(("enter principle amount:")))
# r = float(input("enter rate:"))
# t = float(input("enter time:"))
# simple = (p*r*t)/100
# print(simple)
# a, b = 0, 1
# while b < 50:
#     print(b, end=" ")
#     a, b = b, a + b
#     
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_even = 0
# count_odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print("Number of even numbers:", count_even)
# print("Number of odd numbers:", count_odd)
word = input("Enter a word: ")
reverse_word = word[::-1]
print("Reversed word:", reverse_word)