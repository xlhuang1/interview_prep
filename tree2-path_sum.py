#  Given a binary tree and an integer target, return True if the tree has any root-to-leaf path such that the sum of the node values along the path equals target.

# note - must be root-to-leaf.

def path_sum(root, target):
    if not root:
        return False

    target -= root.val

    if not root.left and not root.right:
        return target == 0

    return path_sum(root.left, target) or path_sum(root.right, target)