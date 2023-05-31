# Reverse a string using a stack data structure

def reverse_string(string):
    stack = []
    reversed_string = ""
    
    for char in string:
        stack.append(char)
    
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
