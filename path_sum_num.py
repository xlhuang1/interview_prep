# You're given the root of a binary tree and an integer targetSum. Your task is to return the number of paths where the sum of the values along the path equals targetSum.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_path_sum_helper(root, target_sum, prefix_sum_hash, current_sum):
    if root is None:
        return 0

    current_sum += root.val
    count = prefix_sum_hash.get((current_sum - target_sum), 0)
    prefix_sum_hash[current_sum] = prefix_sum_hash.get(current_sum, 0) + 1

    count += count_path_sum_helper(root.left, target_sum, prefix_sum_hash, current_sum)
    count += count_path_sum_helper(root.right, target_sum, prefix_sum_hash, current_sum)

    # backtrack because of visiting both nodes
    prefix_sum_hash[current_sum] -= 1
    return count


def count_path_sum(root, target_sum):
    prefix_sum_hash = {0 : 1}
    current_sum = 0
    return count_path_sum_helper(root, target_sum, prefix_sum_hash, current_sum)