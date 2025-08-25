# Implement an algorithm to serialize and deserialize a binary tree.

# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# There is no additional restriction on how your serialization/deserialization algorithm should work.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root

test = TreeNode(10, TreeNode(1), TreeNode(2, TreeNode(3), TreeNode(4)))
c = Codec()
data = c.serialize(test)
print(data)
res = c.deserialize(data)
print(res.val)