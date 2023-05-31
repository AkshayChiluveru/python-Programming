# Implement a queue using the stack data structure

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, value):
        self.in_stack.append(value)
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if self.out_stack:
            return self.out_stack.pop()
        else:
            return None
