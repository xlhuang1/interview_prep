class TreeNode():
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val


def preorder_dfs(root):
    # (root, left, right)
    # 1 2 4 5 3
    if root is not None:
        print(root.value)
        preorder_dfs(root.left)
        preorder_dfs(root.right)


def postorder_dfs(root):
    # (left, right, root)
    if root is not None:
        postorder_dfs(root.left)
        postorder_dfs(root.right)
        print(root.value)


def postorder_flatten(root, current):
    if root is not None:
        postorder_flatten(root.left, current)
        postorder_flatten(root.right, current)
        if current is not None:
            current.right = TreeNode(root.value)
        else:
            return TreeNode(root.value)

def build_tree(arr):
    end = TreeNode(arr.pop)
    for item in arr[::-1]:
        x = TreeNode(item)
        x.right = end
        end = x
    return end


def inorder_dfs(root):
    # left, root, right
    if root is not None:
        inorder_dfs(root.left)
        print(root.value)
        inorder_dfs(root.right)


if __name__ == "__main__":
    myTree = TreeNode("1")
    l1 = TreeNode("2")
    r1 = TreeNode("3")
    myTree.left = l1
    myTree.right = r1
    l2 = TreeNode("4")
    r2 = TreeNode("5")
    myTree.left.left = l2
    myTree.left.right = r2
    '''
            1
        2       3
    4       5            
    '''
    print("preorder")
    preorder_dfs(myTree)
    print("postorder")
    postorder_dfs(myTree)
    print("inorder")
    inorder_dfs(myTree)
    print('postorder flatten')
    x = build_tree([4,5,2,3,1])
    print(x)

