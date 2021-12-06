class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def clear(self):
        self.data.clear()


s = Stack()
s.push(10)
s.push(20)
print(s.pop())
s.push(30)
print(s.peek())
