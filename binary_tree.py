import pprint


class BinaryTree:
    def __init__(self):
        self._root = {}

    def push(self, value):
        node = self._root

        while node:
            if node["value"] > value:
                node = node["left"]
            elif node["value"] < value:
                node = node["right"]
            else:
                return False
        node["value"] = value
        node["left"] = {}
        node["right"] = {}
        return True

    def search(self, value):
        node = self._root
        while node:
            if node["value"] > value:
                node = node["left"]
            elif node["value"] < value:
                node = node["right"]
            else:
                return True
        return False


class OptimizeBinaryTree:
    def __init__(self):
        self._tree = []

    def push(self, value):
        index = 0
        while index < len(self._tree) and self._tree[index] is not None:
            node = self._tree[index]
            if node > value:
                index = index * 2 + 1
            elif node < value:
                index = index * 2 + 2
            else:
                return False
        self._tree.extend([None for _ in range(len(self._tree), index + 1)])
        self._tree[index] = value

    def search(self, value):
        index = 0
        while index < len(self._tree) and self._tree[index] is not None:
            node = self._tree[index]
            if node > value:
                index = index * 2 + 1
            elif node < value:
                index = index * 2 + 2
            else:
                return True
        return False




tree = OptimizeBinaryTree()
tree.push(4)
tree.push(6)
tree.push(2)
tree.push(7)
tree.push(5)
tree.push(3)
tree.push(1)
pprint.pprint(tree.search(9))
