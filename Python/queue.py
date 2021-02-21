from collections import deque

q = deque()

q.appendleft(2)
q.appendleft(4)
q.appendleft(5)
q.appendleft(7)

print(q)

print(q.pop())
print(q.pop())
print()

###################### OR #####################

class Queue:
    
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(7)

print(q.buffer)

print(q.dequeue())
print(q.dequeue())