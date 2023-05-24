def find_char(string):
    len = {}

    for char in string:
        len[char] = len.get(char, 0) + 1

    for char in string:
        if len[char] == 1:
            return char

    return None

input_string = input("Enter a string: ")
result = find_char(input_string)

if result:
    print("The first non-repeated character is:", result)
else:
    print("No non-repeated character found in the string.")
