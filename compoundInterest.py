#python program to find Compund Interest
# A = P(1 + r/n)^nt
# A	=	final amount
# P	=	initial principal balance
# r	=	interest rate
# n	=	number of times interest applied per time period
# t	=	number of time periods elapsed
import math


p = float(input("Enter Initial principal balance: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter number of times elapsed: "))
amt = p * (math.pow((1 + (r/100)),t))
print("Compound Amount: ",amt)
CI = amt - p
print("compound Interest: ",CI)