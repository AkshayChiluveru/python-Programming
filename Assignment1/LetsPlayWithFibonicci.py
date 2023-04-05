n = int(input("Enter a Number :"))
a, b = 0, 1
while a < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c

