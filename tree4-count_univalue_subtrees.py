# Given the root of a binary tree, return the number of univalue subtrees.
# A univalue subtree means all nodes of the subtree have the same value.

def count_univalue_subtrees_helper(root):
    if root is None:
        return 0, True

    left_count, left_is_univalue = count_univalue_subtrees_helper(root.left)
    right_count, right_is_univalue = count_univalue_subtrees_helper(root.right)

    is_univalue = True

    if root.left and (not left_is_univalue or root.left.val != root.val):
        is_univalue = False

    if root.right and (not right_is_univalue or root.right.val != root.val):
        is_univalue = False

    if is_univalue:
        return 1 + left_count + right_count, True
    else:
        return left_count + right_count, False

def count_univalue_subtrees(root):
    count, _ = count_univalue_subtrees_helper(root)
    return count


class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(5)

print(count_univalue_subtrees(root))