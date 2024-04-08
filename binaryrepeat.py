class maxNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def find(root,data):
    if not root:
        return maxNode(data)
    
    if data<root.data:
        root.left=find(root.left, data)
    if data>root.data:
            root.right=find(root.right, data)
    return root

def maxElement(root):
    currentvalue=root

    while(currentvalue.right):
        currentvalue=currentvalue.right
    return currentvalue.data

if __name__=='__main__':
    root=None
    root=find(root,5)
    root=find(root,3)
    root=find(root,7)
    root=find(root,9)
    root=find(root,15)
    print("Maximum value={}".format(maxElement(root)))