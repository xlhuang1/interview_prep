# You are given two integer arrays preorder and inorder.
#
# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)
    root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root
