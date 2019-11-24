# Model
class Deque:
    def __init__(self):
        self._list = []

    def push_back(self, value):
        self._list.insert(0, value)

    def push_front(self, value):
        self._list.append(value)

    def pop_front(self):
        return self._list.pop()

    def pop_back(self):
        return self._list.pop(0)

    def print(self):
        print(*self._list)

    def front(self):
        return self._list[-1]

    def back(self):
        return self._list[0]

    def size(self):
        return len(self._list)

    def clear(self):
        self._list = []

# View
class View:
    def _print(self, val):
        print(val)

    def _input(self):
        return input()

# Controller
class Controller:
    def __init__(self):
        self.stack = Deque()
        self.view = View()

    def execute(self):
        _in = self.view._input()
        if "push_front" in _in:
            m = _in.split()
            self.stack.push_front(m[1])
            self.view._print("ok")
        if "push_back" in _in:
            m = _in.split()
            self.stack.push_back(m[1])
            self.view._print("ok")
        elif _in == "pop_front":
            self.view._print(self.stack.pop_front())
        elif _in == "pop_back":
            self.view._print(self.stack.pop_back())
        elif _in == "front":
            self.view._print(self.stack.front())
        elif _in == "back":
            self.view._print(self.stack.back())
        elif _in == "size":
            self.view._print(self.stack.size())
        elif _in == "clear":
            self.stack.clear()
            self.view._print("ok")
        elif _in == "exit":
            self.view._print("bye")
            return False
        return True

# main
controller = Controller()
while controller.execute():
    pass
