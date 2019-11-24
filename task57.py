class Queue:
    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.insert(0, value)

    def pop(self):
        return self._list.pop()

    def front(self):
        return self._list[-1]

    def size(self):
        return len(self._list)

    def clear(self):
        self._list = []

    def print(self):
        print(*self._list)



class View:
    def _print(self, val):
        print(val)

    def _input(self):
        return input()


class Controller:
    def __init__(self):
        self.stack = Queue()
        self.view = View()

    def execute(self):
        _in = self.view._input()
        if "push" in _in:
            m = _in.split()
            self.stack.push(m[1])
            self.view._print("ok")
        elif _in == "pop":
            self.view._print(self.stack.pop())
        elif _in == "front":
            self.view._print(self.stack.front())
        elif _in == "size":
            self.view._print(self.stack.size())
        elif _in == "clear":
            self.stack.clear()
            self.view._print("ok")
        elif _in == "exit":
            self.view._print("bye")
            return False
        return True


controller = Controller()
while controller.execute():
    pass