# Return the maximum depth of a binary tree.
# 👉 Classic DFS recursion to compute depth from leaves up.

def max_depth(node):
    if not node:
        return 0

    depth = 1 + max(max_depth(node.left), max_depth(node.right))

    return depth