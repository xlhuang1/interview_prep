# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
#
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_of_tree(root: TreeNode, p: TreeNode, q: TreeNode):
    lca = [None]

    def post_order_traverse(node, p, q):
        if node is not None:
            left = right = 0
            if node.left:
                left = post_order_traverse(node.left, p, q)
            if node.right:
                right = post_order_traverse(node.right, p, q)

            mid = node.val == p.val or node.val == q.val

            if mid + left + right >= 2:
                lca[0] = node
                return

            return mid or left or right
    post_order_traverse(root, p, q)
    return lca[0]


def lca_of_bst(root: TreeNode, p: TreeNode, q: TreeNode):
    x, y = p.val, q.val

    def exists(root, value):
        if root is None:
            return False
        node = root
        while node:
            if value > node.val:
                node = node.right
            elif value < node.val:
                node = node.left
            else:
                return node.val == value
        return False

    if not (exists(root, x) and exists(root, y)):
        return None

    node = root
    while node:
        if x < node.val and y < node.val:
            node = node.left
        elif x > node.val and y > node.val:
            node = node.right
        else:
            # middle
            return node
    return None

bst = TreeNode(3)
bst.left = one = TreeNode(1)
bst.right = six = TreeNode(6)
bst.right.left = four = TreeNode(4)
bst.right.right = seven = TreeNode(7)
eight = TreeNode(8)

ans = lca_of_bst(bst, one, seven).val if lca_of_bst(bst, one, seven) is not None else None
print(ans)