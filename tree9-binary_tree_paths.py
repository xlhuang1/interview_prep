# Given a binary tree, return all root-to-leaf paths as strings.
# Input: A binary tree
#
# Output: A list of strings, each representing a path from root to leaf
# e.g., "1->2->5" for a path from node 1 to 2 to 5.


def binary_tree_paths(root):
    paths = []

    def binary_tree_helper(root, path_str):
        if root is None:
            return

        if root.left is None and root.right is None:
            # leaf
            paths.append(path_str+str(root.val))
            return

        path_str = path_str+str(root.val)+"->"
        binary_tree_helper(root.left, path_str)
        binary_tree_helper(root.right, path_str)

    binary_tree_helper(root, "")
    return paths