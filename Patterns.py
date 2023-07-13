# square pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*" , end=" ")
#     print()


# right angled triangle:
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()


# printing odd number of patterns

# n = 5
# k = 1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("*" , end=" ")
#     k = k + 2
#     print()


# triangle
# n =5
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# odd number of triangle paattern

# n =5
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,2*i+1):
#         print("*",end="")
#     print()

# reverse triangle pattern

# n = 5
# for i in range(0,n):
#     for j in range(0,i):
#         print(end=" ")
#     for j in range(0,n-i):
#         print("*",end=" ") 
#     print()

# diamond 

# n =5
# for i in range(0,n-1):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# for i in range(0,n):
#     for j in range(0,i):
#         print(end=" ")
#     for j in range(0,n-i):
#         print("*",end=" ") 
#     print()

# reversed right angle triangle 
# n = 5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("*",end=" ")
#     print()

# reverse left angle triangle
# n = 5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for j in range(0,n-i):
#         print("*",end=" ")
#     print()



# left angled triangle
# n = 5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()




# numbers pattern
# n = int(input("Enter the number: "))
# num = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num, end=" ")
#         num = num+1
#     print()


# string pattern program 

string = input("Enter the string: ")
l = len(string)
for i in range(l):
    for j in range(i+1):
        print(string[j], end=" ")
    print()

