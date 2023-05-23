def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1

    if str2 in temp:
        return True
    else:
        return False


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if are_rotations(string1, string2):
    print("The two strings are rotations of each other.")
else:
    print("The two strings are not rotations of each other.")
