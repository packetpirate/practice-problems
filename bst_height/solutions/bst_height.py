# Supporting class for testing purposes.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# This function finds the height of the given BST.
def nodeHeight(root):
    if root != None:
        l = nodeHeight(root.left)
        r = nodeHeight(root.right)
        return max(l,r) + 1
    else: return -1
