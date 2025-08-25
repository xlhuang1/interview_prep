# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them.
# A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    if not root:
        return 0
    max_sum_seen = [root.val]

    def dfs_gain(node):
        if node is None:
            return 0

        left_gain = max(0, dfs_gain(node.left))
        right_gain = max(0, dfs_gain(node.right))

        gain = node.val + max(left_gain, right_gain)
        max_sum_seen[0] = max(max_sum_seen[0], node.val + left_gain + right_gain)
        return gain

    dfs_gain(root)
    return max_sum_seen[0]


testTree = TreeNode(10, TreeNode(9), TreeNode(7, TreeNode(8)))
print(max_path_sum(testTree))