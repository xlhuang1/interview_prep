# first try

# from collections import queue
#
# class TreeNode():
#     value = None
#     left = None
#     right = None
#
#     def __init__(self, val):
#         self.value = val
#
#
# def generate_right_side_view(root):
#     q = queue.Queue()
#     view = [root.value]
#     level = 0
#
#     q.put(root.left)
#     q.put(root.right)
#
#
#     while q.empty() is not True:
#         node = q.get()
#         q.put(node.left)
#         q.put(node.right)
#
#         if node.right is not None:
#             view.append(node.right.value)
#
#     return view

# corrected
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def generate_right_side_view(root):
    if not root:
        return []

    q = deque([root])
    view = []

    while q:
        level_length = len(q)
        for i in range(level_length):
            node = q.popleft()

            # If it's the last node in the level, add to view
            if i == level_length - 1:
                view.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return view

#       1
#       / \
#     2     3
#       \    \
#       5     4
#      / \
#     4   6
#    /
#   7


# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(6)

root.left.right.left.left = TreeNode(7)

# Run the test
print(generate_right_side_view(root))  # Expected output: [1, 3, 4, 6, 7]