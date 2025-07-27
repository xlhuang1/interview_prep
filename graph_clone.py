# You're given a reference to a node in a connected undirected graph. Each node contains a value (int) and a list of its neighbors.

# Your task is to return a deep copy (clone) of the graph.

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
    queue = deque([node])
    visited = {}
    if not node:
        return None

    while queue:
        innerNode = queue.popleft()

        if innerNode not in visited:
            clonedNode = Node(innerNode.val)
            visited[innerNode] = clonedNode
        else:
            clonedNode = visited[innerNode]

        for neighbor in innerNode.neighbors:
            if neighbor not in visited:
                newNeighbor = Node(neighbor.val)
                visited[neighbor] = newNeighbor
                queue.append(neighbor)
            else:
                newNeighbor = visited[neighbor]
            clonedNode.neighbors.append(newNeighbor)

    return visited[node]

# test harness ##################
def build_graph(adj_list):
    """Builds a graph from an adjacency list."""
    if not adj_list:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj_list) + 1)}
    for i, neighbors in enumerate(adj_list, 1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]

def serialize_graph(node):
    """Converts a graph into an adjacency list for comparison."""
    if not node:
        return []
    result = {}
    visited = set()
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        if curr.val in visited:
            continue
        visited.add(curr.val)
        result[curr.val] = [n.val for n in curr.neighbors]
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)
    return [result[i] for i in range(1, len(result) + 1)]

def test_cloneGraph():
    test_cases = [
        ([[2,4],[1,3],[2,4],[1,3]], "4-node square"),
        ([[2],[1]], "2-node single edge"),
        ([[2,3],[1],[1]], "3-node star"),
        ([], "empty graph"),
        ([[1]], "self-loop")
    ]

    for adj_list, name in test_cases:
        print(f"Testing {name}...")
        original = build_graph(adj_list)
        cloned = cloneGraph(original)
        orig_serialized = serialize_graph(original)
        clone_serialized = serialize_graph(cloned)
        assert orig_serialized == clone_serialized, f"Mismatch in {name}"
        print("✅ Passed")

test_cloneGraph()
