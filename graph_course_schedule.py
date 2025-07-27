# You're given a list of course prerequisites in the form of pairs:
# [a, b] means to take course a, you must first take course b.
#
# You’re also given the total number of courses numCourses.

# Write a function that returns True if it is possible to finish all courses, and False if there is a cycle (i.e., circular dependency).
from collections import defaultdict
from collections import deque


def create_dag(array: list[list[int]]):
    # list of destinations for source node
    graph = defaultdict(list)
    for dest, src in array:
        graph[src].append(dest)
    return graph

def count_in_degrees(graph, numCourses):
    inc_edges = {i : 0 for i in range(numCourses)}
    for src, dst_list in graph.items():
        for dest in dst_list:
            inc_edges[dest] += 1
    return inc_edges

def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    dag = create_dag(prerequisites)
    incoming_edges = count_in_degrees(dag, numCourses)

    queue = deque()
    for node, inc in incoming_edges.items():
        if inc == 0:
            queue.append(node)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in dag[node]:
            incoming_edges[neighbor] -= 1
            if incoming_edges[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == numCourses

print(can_finish(2, [[1, 0]]))  # → True
print(can_finish(2, [[1, 0], [0, 1]]))  # → False