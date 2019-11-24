class Deque:
    def __init__(self):
        self._list = []

    def push_first(self, value):
        self._list.insert(0, value)

    def push_last(self, value):
        self._list.append(value)

    def pop_first(self):
        return self._list.pop(0)

    def pop_last(self):
        return self._list.pop()

    def print(self):
        print(*self._list)


deque = Deque()
deque.push_first(10)
deque.push_last(20)
deque.push_first(15)
deque.push_last(-3)
deque.pop_first()
deque.push_last(18)
deque.pop_first()
deque.pop_last()
deque.print()
