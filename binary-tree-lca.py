class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_lca(root, p, q):
    lca = [None]

    def post_order_traversal(node, p, q):
        if node is not None:
            left = right = 0
            if node.left:
                left = post_order_traversal(node.left, p, q)
            if node.right:
                right = post_order_traversal(node.right, p, q)

            mid = node.val == p or node.val == q

            if mid + left + right >= 2:
                lca[0] = node

            return mid or left or right

    post_order_traversal(root, p, q)
    return lca[0]

bst = TreeNode(3)
bst.left = TreeNode(1)
bst.right = TreeNode(6)
bst.right.left = TreeNode(4)
bst.right.right = TreeNode(7)

print(find_lca(bst, 1, 4).val)
