class TreeNode():
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val

def breadth_first_traversal(root):
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        if node is not None:
            print(node.value)
            q.append(node.left)
            q.append(node.right)




if __name__ == "__main__":
    '''
            1
        2       3
    4       5            
    '''
    myTree = TreeNode("1")
    l1 = TreeNode("2")
    r1 = TreeNode("3")
    myTree.left = l1
    myTree.right = r1
    l2 = TreeNode("4")
    r2 = TreeNode("5")
    myTree.left.left = l2
    myTree.left.right = r2
    print("bfs")
    breadth_first_traversal(myTree)