# graph problem - given n nodes labeled 0 to n-1 and a list of undirected edges, return number of connected components in graph
# n = 5
# edges = [[0, 1], [1, 2], [3, 4]]

from collections import defaultdict, deque

# try 1
def get_other_element(x, l):
    # size 2 - return other member of edge
    if l[0] == x:
        return l[1]
    else:
        return l[0]

def count_components(n: int, edges: list[list[int]]) -> int:
    visited = set()
    component_count = 0
    for i in range(0, n):
        if i not in visited:
            visited.add(i)
            component_count += 1
            search = i
            for edge in edges:
                if search in edge:
                    j = get_other_element(i, edge)
                    if j not in visited:
                        visited.add(j)
                        search = j
    return component_count


# try 2
def count_components(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    component_count = 0


    for i in range(0, n):
        if i not in visited:
            component_count += 1
            que = deque([i])
            visited.add(i)

            while que:
                node = que.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        que.append(neighbor)

    return component_count

