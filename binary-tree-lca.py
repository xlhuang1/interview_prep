class TreeNode():
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val


def find_lca(root, p, q):
    lca = [None]

    def post_order_traversal(node, p, q):
        if node is not None:
            left = post_order_traversal(node.left)
            right = post_order_traversal(node.right)

            mid = node.value == p or node.value == q

            if mid + left + right >= 2:
                lca[0] = node

            return mid or left or right

    post_order_traversal(root, p, q)
    return lca[0]