a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))

print("The number before swapped A: ", a)
print("The number before swapped B: ", b)

# Approch 1
# temp = a
# a = b 
# b = temp

# Approch 2
a,b = b,a

print("The number after swapped A: ", a)
print("The number after swapped B: ", b)