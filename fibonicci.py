n1= int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n3 = int(input("Enter the range: "))
print(n1,n2)

for i in range(0,n3+1):
    sum = n1 + n2 
    print(sum,end=" ")
    n1 = n2
    n2 = sum