# Problem: Each root-to-leaf path represents a number formed by concatenating the node values along the path. Return the total sum of all such numbers.
#     1
#    / \
#   2   3
# Paths: 1->2 (number 12), 1->3 (number 13).
# Answer: 12 + 13 = 25.

def sum_root_helper(root, curr_num):
    if not root:
        return 0

    new_val = curr_num * 10 + root.val
    if not root.left and not root.right:
        return new_val
    final_val = sum_root_helper(root.left, new_val) + sum_root_helper(root.right, new_val)
    return final_val


def sum_of_root_to_leaf_numbers(root):
    return sum_root_helper(root, 0)