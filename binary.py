class binaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")




root = binaryTree("Furniture")
nodeA = binaryTree("Couch")
nodeB = binaryTree("Table")
nodeC = binaryTree("Stool")
nodeD = binaryTree("Drawer")
nodeE = binaryTree("Seat")
nodeF = binaryTree("Pillow")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

print("postOrderTraversal:")
postOrderTraversal(root)


