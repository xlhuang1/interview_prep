# Given the root of a binary tree and an integer targetSum,
# return True if the tree has any root-to-leaf path such that the sum of the node values along the path equals targetSum.

def path_sum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum-root.val == 0

    left = path_sum(root.left, targetSum-root.val)
    right = path_sum(root.right, targetSum-root.val)

    return left or right