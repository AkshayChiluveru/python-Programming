def is_operator(char):
    """Check if a character is an operator."""
    return char in "+-*/^"

def postfix_to_prefix(expression):
    """Convert a postfix expression to a prefix expression."""
    stack = []

    for char in expression:
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()

            prefix = char + operand2 + operand1

            stack.append(prefix)
        else:
            stack.append(char)

    return stack.pop()

postfix = input("Enter the postfix expression: ")

prefix = postfix_to_prefix(postfix)

print("Prefix expression:", prefix)
