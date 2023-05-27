def is_operator(char):
    """Check if a character is an operator."""
    return char in "+-*/^"

def prefix_to_infix(expression):
    """Convert a prefix expression to an infix expression."""
    stack = []

    for char in reversed(expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()

            infix_expression = '(' + operand1 + char + operand2 + ')'

            stack.append(infix_expression)
        else:
            stack.append(char)

    return stack.pop()

prefix_expression = input("Enter the prefix expression: ")


infix_expression = prefix_to_infix(prefix_expression)

print("Infix expression:", infix_expression)
