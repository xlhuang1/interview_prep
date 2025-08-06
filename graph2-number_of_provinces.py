# Number of Provinces
# You're given an n x n adjacency matrix isConnected, where isConnected[i][j] = 1 means city i and city j are directly connected.
# A province is a group of directly or indirectly connected cities.
#
# 👉 Goal: Return the total number of provinces.

from collections import deque, defaultdict

def build_adjacency_list(isConnected):
    graph = defaultdict(list)
    rows = len(isConnected)
    cols = len(isConnected[0]) if isConnected else 0
    for r in range(rows):
        for c in range(r + 1, cols):
            if isConnected[r][c] == 1:
                graph[r].append(c)
                graph[c].append(r)
    return graph

def count_provinces(isConnected):
    visited = set()
    queue = deque()
    count_of_provinces = 0
    adj_graph = build_adjacency_list(isConnected)

    n = len(isConnected)

    for i in range(n):
        if i not in visited:
            visited.add(i)
            queue.append(i)
            count_of_provinces += 1
        while queue:
            node = queue.popleft()
            for neighbor in adj_graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return count_of_provinces