# # Square pattern

# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# # right angled triangle

# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# # Decreasing right angled triangle

# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()



# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()



#  practicing patters

# square

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("#" , end=" ")
#     print()


# right triangle
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("#" , end=" ")
#     print()


# right downward triangle
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("#" , end=" ")
#     print()



# left triangle 

# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(" " , end=" ")
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()


# left downward triangle
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" " , end=" ")
#     for j in range(n-i):
#         print("*" , end=" ")
#     print()


#  Triangle

n = 5
for i in range(n):
    for j in range(n-i):
        print(" " , end="")
    for j in range(i+1):
        print("*" , end=" ")
    print()