# ➤ Undirected graph. Given n nodes and edge list, check if path exists from source to destination.

from collections import defaultdict, deque

def convert_graph(edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def path_exists(source, destination, n, edges):
    graph = convert_graph(edges)
    queue = deque([source])
    visited = {source}

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        if node in graph:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return False
