def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)

my_string = "The quick Brow Fox"
upper_count, lower_count = count_upper_lower(my_string)
print("No. of Upper case characters :", upper_count)  # Output: 3
print("No. of Lower case Characters :", lower_count)