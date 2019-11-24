class Queue:
    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.insert(0, value)

    def pop(self):
        return self._list.pop()

    def print(self):
        print(*self._list)


queue = Queue()
queue.push(10)
queue.push(20)
queue.push(15)
queue.push(-3)
queue.pop()
queue.push(18)
queue.pop()
queue.pop()
queue.print()