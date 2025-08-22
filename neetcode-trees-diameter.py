# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root):

    def dfs_height(node):
        if node is None:
            return 0

        l_height = r_height = 0
        if node.left is not None:
            l_height = 1 + dfs_height(node.left)
        if node.right is not None:
            r_height = 1 + dfs_height(node.right)

        max_diam_seen[0] = max(max_diam_seen[0], l_height + r_height)

        return max(l_height, r_height)

    max_diam_seen = [0]
    dfs_height(root)
    return max_diam_seen[0]


def diameter_iterative(root):
    """
    Diameter measured in EDGES.
    Iterative post-order using a single stack with a visited flag.
    """
    if root is None:
        return 0

    stack = [(root, False)]
    height = {}     # node -> height in edges from node to deepest leaf (leaf: 0)
    max_diam = 0

    while stack:
        node, seen = stack.pop()
        if node is None:
            continue
        if not seen:
            # Post-order: push node back as 'seen', then its children
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            # Children already processed -> their heights known
            lh = height[node.left] + 1 if node.left else 0
            rh = height[node.right] + 1 if node.right else 0

            # Longest path through this node (in edges)
            max_diam = max(max_diam, lh + rh)

            # Height for this node (in edges): 0 if leaf, else 1 + max child
            height[node] = max(lh, rh)

    return max_diam

testTree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
print(diameter(testTree))
print(diameter_iterative(testTree))

testTree2 = TreeNode(1)
testTree2.left = TreeNode(2)
testTree2.left.left = TreeNode(3)
testTree2.left.left.right = TreeNode(4)

print(diameter(testTree2))
print(diameter_iterative(testTree2))