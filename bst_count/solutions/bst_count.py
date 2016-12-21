# Supporting class for testing purposes.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# This function will count how made nodes are in a given BST.
def nodeCount(root):
    if root != None:
        return nodeCount(root.left) + 1 + nodeCount(root.right)
    else: return 0
