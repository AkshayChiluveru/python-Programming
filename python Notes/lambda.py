# python lambda

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:

x = lambda x: x +10
print(x(5))

x = lambda x: x *10
print(x(5))

x1 = lambda x,y: x +y
print(x1(5,6))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# def myfunc(n):
#   return lambda a : a * n


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))