num = int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
    # print(fact)

print(fact)

# Using funtions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter the number: "))
print(factorial(num))




