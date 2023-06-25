# Python Program to Find the sum of N natural Numbers Using while loop

# for --> loops are basically used when we know the number of iterations or sequence.
# while loop--> if we want to execute a group of statement based on certain condition.

# i=0
# sum=0
# n=int(input("Enter the number"))
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

# using for loop:

N = int(input("Enter a number:"))
sum = 0
for i in range(N+1):
    sum = sum + i
print(sum)
