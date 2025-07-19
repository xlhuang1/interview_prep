# first try
from collections import deque

class TreeNode():
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val

class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.iter_queue = deque()
        self.populate_iter_queue(root)

    def next(self) -> int:
        # return next smallest number
        return self.iter_queue.popleft()

    def hasNext(self):
        # returns True if there exists a next number
        return len(self.iter_queue) > 0

    def populate_iter_queue(self, node):
        if not node:
            return
        self.populate_iter_queue(node.left)
        self.iter_queue.append(node.value)
        self.populate_iter_queue(node.right)

