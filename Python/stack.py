from collections import deque

stack = deque()
# print(dir(stack))

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.peek())
    print(s.peek())
