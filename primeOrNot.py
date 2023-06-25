n = int(input("Enter the Number: "))
if n == 1:
    print("it is neither prime nor composite")
elif n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")    
        
