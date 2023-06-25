# odd even without using functions
n = int(input("Enter the Number: "))
if n%2==0:
    print("It is an even Number")
else:
     print("It is an odd Number")


#odd even using functions
def odd_even(number):
    if number%2==0:
        return "It is an even Number"
    else:
        return "It is an odd Number"
number=int(input("Enter a number: "))
print(odd_even(number))

