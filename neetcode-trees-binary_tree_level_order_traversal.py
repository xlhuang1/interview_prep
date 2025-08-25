# Given a binary tree root, return the level order traversal of it as a nested list,
# where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Input: root = [1,2,3,4,5,6,7]
# Output: [[1],[2,3],[4,5,6,7]]
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root) -> List[List[int]]:
    if root is None:
        return []
    result = []

    queue = deque([root])

    while queue:
        level = len(queue)
        current_arr = [None] * level
        for i in range(level):
            node = queue.popleft()
            current_arr[i] = node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(current_arr)
    return result


test_root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(level_order(test_root))