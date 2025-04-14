class Stack_op():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, x):
        return self.stack.append(x)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def seek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

# Using the class
s = Stack_op()
s.push(10)
print(s.seek())
s.push(20)
print(s.seek())
s.push(30)
print(s.seek())
s.pop()   
print(s.seek())
s.pop()    # Removes 20
print(s.seek())  # Should return 10 (top element)
