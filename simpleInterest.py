#python program to find simple interest
# A = (p*t*r)/100
# A	=	final amount
# P	=	initial principal balance
# r	=	annual interest rate
# t	=	time (in years)
p = int(input("Enter Initial principal balance: "))
r = int(input("Enter annual interest rate: "))
t = int(input("Enter time: "))
a = (p*t*r)/100
print("Final Amount: " ,a)

