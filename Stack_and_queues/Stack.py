# example of stack:

def add(a, b):
    return a + b

def f():
    x = 4
    y = 5
    return add(x, y)

f()

class Stack:
    def __init__(self):
        self.data = None

    def push(self, value):
        # Array: O(1)
        self.data.append(value)

    def pop(self):
        # Array: O(1)
        return self.data.pop()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.data
# //=> [1,2,3]
s.pop()
# //=> 3