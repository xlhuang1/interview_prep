# visible nodes - for every level there must be at least 1 visible node unless it is composed entirely of leafs
# this problem simplifies down into the max height of the tree
from collections import deque

class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    # Add any helper functions you may need here


def visible_nodes(root):
    # Write your code here
    if root is None:
        return 0
    return 1 + max(visible_nodes(root.left), visible_nodes(root.right))


def visible_nodes_left_values(root):
    # if we expand this to return the actual visible nodes at every level as viewed from the left

    view = []
    if root is None:
        return view

    queue = deque([root])

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()

            if i == 0:
                # furthest left -> add to view
                view.append(node.val)
            # add all children of node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view


def visible_nodes_left_values_dfs(root):
    view = []

    def dfs(node, level):
        if not node:
            return
        if level == len(view):
            # add to view if this is the first node seen on this level (furthest left)
            view.append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return view


def visible_nodes_right_values_dfs(root):
    view = []

    def dfs(node, level):
        if node is None:
            return

        if level == len(view):
            # append first node seen on level
            view.append(node.val)

        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return view

print(visible_nodes_left_values_dfs(TreeNode(5)))