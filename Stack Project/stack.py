class Stack:      
    def __init__(self):
        self.stack = []
        self.size =  0
    
    def push(self, item):
        self.size += 1
        return self.stack.append(item)
    
    def pop(self):
        if self.size == 0:
            raise IndexError("Cannot pop if the stack is empty.")
        self.size -= 1
        return self.stack.pop()
    
    def top(self):
        if self.size == 0:
            raise IndexError("There is no top.")
        return self.stack[self.size-1]
    
    def __len__(self):
        return self.size
    
    def clear(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)