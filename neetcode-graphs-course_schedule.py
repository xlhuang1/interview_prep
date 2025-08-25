# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
#
# The pair [0, 1], indicates that must take course 1 before taking course 0.
#
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
#
# Return true if it is possible to finish all courses, otherwise return false.
from collections import deque

def can_finish(numCourses, prerequisites):

    def make_graph(prerequisites):
        # DAG where (u, v) means that u -> v in terms of prereqs, u is a prereq of v
        # key of graph is class u and value of graph is list of classes v for which u is prereq
        g = {}
        for v, u in prerequisites:
            if u not in g:
                g[u] = [v]
            elif u in g:
                g[u].append(v)
        return g

    graph = make_graph(prerequisites)
    in_deg_counts = {i: 0 for i in range(numCourses)}
    for _, dest_list in graph.items():
        for dst in dest_list:
            in_deg_counts[dst] += 1

    queue = deque([])
    for node in in_deg_counts.keys():
        if in_deg_counts[node] == 0:
            queue.append(node)

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node in graph:
            for neighbor in graph[node]:
                in_deg_counts[neighbor] -= 1
                if in_deg_counts[neighbor] == 0:
                    queue.append(neighbor)
    return len(order) == numCourses


