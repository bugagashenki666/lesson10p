def depth_python_recursive(graph, start, target, visited=None):
    print("depth_python_recursive current: ", start)
    if start == target:
        return True
    if visited is None:
        visited = set()
    visited.add(start)

    for vertex in graph[start]:
        if vertex == target or (vertex not in visited and depth_python_recursive(graph, vertex, target, visited)):
            return True
    return False


def depth_pyhton(graph, start, target):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        print("depth_python: ", vertex)
        visited.add(vertex)
        if vertex == target:
            return True
        for v in graph[vertex]:
            if v == target:
                return True
            elif v not in visited:
                stack.append(v)
    return False


def depth_recursive(graph, start, target, visited=None):
    print("depth_recursive current: ", start)
    if start == target:
        return True
    if visited is None:
        visited = set()
    visited.add(start)

    for vertex, value in enumerate(graph[start]):
        if value == 1:
            if vertex == target or (vertex not in visited and depth_recursive(graph, vertex, target, visited)):
                return True
    return False


def depth(graph, start, target):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        print("depth current: ", vertex)
        visited.add(vertex)
        if vertex == target:
            return True
        for v, value in enumerate(graph[vertex]):
            if value == 1:
                if v == target:
                    return True
            elif v not in visited:
                stack.append(v)
    return False


def width_python(graph, start, target):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop()
        print("width current: ", vertex)
        visited.add(vertex)
        if vertex == target:
            return True

        for v in graph[vertex]:
            if v == target:
                return True
            elif v not in visited and v not in queue:
                queue.insert(0, v)
    return False


def width(graph, start, target):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop()
        print("width current: ", vertex)
        visited.add(vertex)
        if vertex == target:
            return True

        for v, value in enumerate(graph[vertex]):
            if value == 1:
                if v == target:
                    return True
                elif v not in visited and v not in queue:
                    queue.insert(0, v)
    return False


graph_pyton = {
    "A": ("B"),
    "B": ("C",),
    "C": ("A", "D"),
    "D": ("B",),
    "E": ("C",),
    "F": (),
    "G": ("D", "E", "F"),
}

graph = (
    (0, 1, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0),
    (1, 0, 0, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 0),
)

print(depth_python_recursive(graph_pyton, "A", "F"))
print(depth_pyhton(graph_pyton, "A", "F"))

print(depth_python_recursive(graph_pyton, "G", "A"))
print(depth_pyhton(graph_pyton, "G", "A"))

print(depth_recursive(graph, 6, 0))
print(depth(graph, 6, 0))

print(width_python(graph_pyton, "G", "A"))
print(width_python(graph_pyton, "A", "F"))


print(width(graph, 6, 0))