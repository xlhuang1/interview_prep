# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    if not root:
        return []

    view = []
    queue = deque([root])

    while queue:
        level = len(queue)
        for i in range(level):
            node = queue.popleft()
            if i == level-1:
                view.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return view


test = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))
print(right_side_view(test))