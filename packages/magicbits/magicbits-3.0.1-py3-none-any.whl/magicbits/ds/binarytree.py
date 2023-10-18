class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key
    
def printInorder(root: Node):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)
def printPostorder(root: Node):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)
def printPreorder(root: Node):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is : ")
    printPreorder(root)
    print("Inorder traversal of binary tree is : ")
    printInorder(root)
    print("Postorder traversal of binary tree is :")
    printPostorder(root)
