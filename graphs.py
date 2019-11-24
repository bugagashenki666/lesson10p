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
                stack.append(0, v)
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

print(depth_python_recursive(graph_pyton, "A", "F"))
print(depth_pyhton(graph_pyton, "A", "F"))


print(depth_python_recursive(graph_pyton, "G", "A"))
print(depth_pyhton(graph_pyton, "G", "A"))
