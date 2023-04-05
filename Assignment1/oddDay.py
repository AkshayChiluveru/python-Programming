numbers = int(input("Enter Number : "))
even = 0
odd = 0
for num in range (1,numbers+1):
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)