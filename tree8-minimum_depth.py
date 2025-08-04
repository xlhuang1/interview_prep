# Minimum Depth of Binary Tree
# Leetcode 111
# 👉 Compute the minimum number of nodes from root to the nearest leaf node. Use DFS.

def min_depth(root):
    if root is None:
        return 0

    if root.left is None:
        return 1 + min_depth(root.right)
    if root.right is None:
        return 1 + min_depth(root.left)

    return 1 + min(min_depth(root.left), min_depth(root.right))