# first try

class TreeNode():
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val

# def check_bst_helper(node, min_val, max_val):
#     if node is None:
#         # bottom of tree
#         return True
#
#     if node.left:
#         if node.left.value > node.value:
#             return False
#         else:
#             check_bst_helper(node.left, node.value, max_val)
#     if node.right:
#         if node.right.value < node.value:
#             return False
#         else:
#             check_bst_helper(node.right, min_val, node.value)
#
#
#
# def is_valid_bst(root: TreeNode) -> bool:
#     min_val = float('-inf')
#     max_val = float('inf')
#     is_valid = check_bst_helper(root, min_val, max_val)
#     return is_valid

# second try
def check_bst_helper(node, min_val, max_val):
    if node is None:
        # bottom of tree
        return True

    if not (min_val < node.value < max_val):
        return False

    return (check_bst_helper(node.left, min_val, node.value) and check_bst_helper(node.right, node.value, max_val))


def is_valid_bst(root: TreeNode) -> bool:
    min_val = float('-inf')
    max_val = float('inf')
    return check_bst_helper(root, min_val, max_val)