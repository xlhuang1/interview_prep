# 1. Invert Binary Tree
# Leetcode 226
# Problem: Flip the tree left↔right at every node.
# Concepts: Recursion, tree mutation.

def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    root.left = invert_tree(root.left)
    root.right = invert_tree(root.right)

    return root