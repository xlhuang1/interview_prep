# Check if Two Binary Trees are the Same
# Leetcode 100
# 👉 Recursively compare both structure and node values.

def both_trees_same(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    elif root1.val != root2.val:
        return False

    return both_trees_same(root1.left, root2.left) and both_trees_same(root1.right, root2.right)