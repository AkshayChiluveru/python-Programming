def are_brackets_balanced(code):
    """Check if all brackets are balanced and closed in the code snippet."""
    stack = []

    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False

            top_bracket = stack.pop()

            if opening_brackets.index(top_bracket) != closing_brackets.index(char):
                return False

    return len(stack) == 0

code_snippet = input("Enter the code snippet: ")

if are_brackets_balanced(code_snippet):
    print("All brackets are balanced and closed.")
else:
    print("Some brackets are not balanced or closed.")
