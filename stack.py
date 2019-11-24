class Stack:
    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.append(value)

    def pop(self):
        return self._list.pop()

    def print(self):
        print(*self._list)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(15)
stack.push(-3)
stack.pop()
stack.push(18)
stack.pop()
stack.pop()
stack.print()
