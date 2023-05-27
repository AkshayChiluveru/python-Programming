class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def reverse(self):
        if self.is_empty():
            return

        temp_stack = Stack()
        while not self.is_empty():
            temp_stack.push(self.pop())

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


stack_input = input("Enter the stack elements: ")

stack = Stack()
elements = stack_input.split()
for element in elements:
    stack.push(element)

stack.reverse()

print("Reversed stack:")
while not stack.is_empty():
    print(stack.pop())
