# The diameter of a binary tree is the length of the longest path between any two nodes, measured by the number of edges in that path.
# Find the diameter of a binary tree.


def diameter(root):
    if not root:
        return 0

    max_diameter_seen = [0]

    def height(root):
        if not root:
            return 0

        left_height = right_height = 0

        if root.left is not None:
            left_height = 1 + height(root.left)
        if root.right is not None:
            right_height = 1 + height(root.right)

        max_diameter_seen[0] = max(max_diameter_seen[0], left_height + right_height)

        return max(left_height, right_height)

    height(root)
    return max_diameter_seen[0]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_tuple(data):
    """ Helper to build a binary tree from nested tuples: (val, left, right) """
    if data is None:
        return None
    val, left, right = data
    node = TreeNode(val)
    node.left = build_tree_from_tuple(left)
    node.right = build_tree_from_tuple(right)
    return node

trees = {
    "empty tree": (None, 0),
    "single node": ((1, None, None), 0),
    "two nodes": ((1, (2, None, None), None), 1),
    "balanced tree": ((1, (2, (4, None, None), (5, None, None)), (3, None, None)), 3),
    "linear chain": ((1, (2, (3, (4, None, None), None), None), None), 3),
}

for name, (tree_data, expected) in trees.items():
    root = build_tree_from_tuple(tree_data)
    result = diameter(root)
    print(f"{name}: expected {expected}, got {result} — {'PASS' if result == expected else 'FAIL'}")
