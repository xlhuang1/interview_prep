# Given the root of a binary tree and an integer targetSum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. Otherwise, return False.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum_helper(root, target_sum, current_sum, seen_prefix_sums):
    if root is not None:
        current_sum += root.val
        seen_prefix_sums[current_sum] = seen_prefix_sums.get(current_sum, 0) + 1
        if (current_sum - target_sum) in seen_prefix_sums:
            return True
        else:
            left_res = has_path_sum_helper(root.left, target_sum, current_sum, seen_prefix_sums)
            right_res = has_path_sum_helper(root.right, target_sum, current_sum, seen_prefix_sums)
            seen_prefix_sums[current_sum] -= 1
            return left_res or right_res

    else:
        return False

def has_path_sum(root: TreeNode, targetSum: int) -> bool:
    if root is not None:
        current_sum = 0
        seen_prefix_sums = {0 : 1}
        return has_path_sum_helper(root, targetSum, current_sum, seen_prefix_sums)
    else:
        return False