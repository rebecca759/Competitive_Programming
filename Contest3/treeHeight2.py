class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        

def findHeight(root):
    if not root:
        return -1
    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)

    return max(leftHeight,rightHeight)+1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.left = Node(6)

print(findHeight(root))
