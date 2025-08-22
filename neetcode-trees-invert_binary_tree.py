# You are given the root of a binary tree root. Invert the binary tree and return its root.
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [1,3,2,7,6,5,4]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

