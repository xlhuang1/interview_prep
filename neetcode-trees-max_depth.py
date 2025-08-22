# Given the root of a binary tree, return its depth.
#
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    depth = 0
    while queue:
        depth += 1
        level = len(queue)
        for i in range(level):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return depth


testTree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
print(max_depth_bfs(testTree))

testTree2 = TreeNode(1)
testTree2.left = TreeNode(2)
testTree2.left.left = TreeNode(3)
testTree2.left.left.right = TreeNode(4)

print(max_depth_bfs(testTree2))