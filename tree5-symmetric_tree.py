# 5. Symmetric Tree
# Leetcode 101
#
# Check if tree is a mirror of itself.
# 👉 Recursive helper to compare left vs. right subtree symmetry.

def is_symmetric(root):
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# === Test Cases ===

# Symmetric: [1, 2, 2, 3, 4, 4, 3]
tree1 = TreeNode(1,
                 TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(2, TreeNode(4), TreeNode(3)))

# Asymmetric structure: [1, 2, 2, None, 3, None, 3]
tree2 = TreeNode(1,
                 TreeNode(2, None, TreeNode(3)),
                 TreeNode(2, None, TreeNode(3)))

# Asymmetric value: [1, 2, 2, 3, 4, 4, 5]
tree3 = TreeNode(1,
                 TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(2, TreeNode(4), TreeNode(5)))

# Single node
tree4 = TreeNode(1)

# Empty tree
tree5 = None

# Run tests
trees = [tree1, tree2, tree3, tree4, tree5]
expected = [True, False, False, True, True]

for i, (tree, exp) in enumerate(zip(trees, expected), 1):
    result = is_symmetric(tree)
    print(f"Test {i}: Expected {exp}, Got {result} - {'✅' if result == exp else '❌'}")