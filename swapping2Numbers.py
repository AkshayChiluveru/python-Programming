a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))

temp = a
a = b 
b = temp

print("The number after swapped A: ", a)
print("The number after swapped B: ", b)