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

    def get_min(self):
        if self.is_empty():
            return None
        return min(self.items)


stack_input = input("Enter the stack elements: ")
stack = Stack()
elements = stack_input.split()
for element in elements:
    stack.push(int(element))

smallest_number = stack.get_min()

if smallest_number is not None:
    print("Smallest number in the stack:", smallest_number)
else:
    print("Stack is empty.")
