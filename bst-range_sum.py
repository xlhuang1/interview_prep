# Range Sum of BST
# Leetcode 938
# Sum all node values in a BST in range [L, R].

def range_sum(root, l, r):
    if root is None:
        return 0

    if root.val < l:
        return range_sum(root.right, l, r)
    elif l <= root.val <= r:
        return root.val + range_sum(root.left, l, r) + range_sum(root.right, l, r)
    else:
        return range_sum(root.left, l, r)