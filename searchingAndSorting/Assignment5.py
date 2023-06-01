# askdWrite a program to sort list of strings (similar to that of dictionary)


strings = input("Enter the list of strings: ").split(',')
strings = [s.strip() for s in strings]  # Trim leading/trailing spaces

strings.sort()
print("Sorted list of strings:", strings)
