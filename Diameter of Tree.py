class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root==None:
        return
    
    else:
        print(root.data,end = ':')
        
        if root.left != None:
            print("L",root.left.data,end = ',')
        if root.right != None:
            print("R",root.right.data,end = '')

        print()
        printTree(root.left)
        printTree(root.right)

def InputTree():
    rootData = int(input())
    
    if rootData == -1: # If -1 is the input, stop the recursive call into that node's left or right
        return None
    
    rootNode = BinaryTreeNode(rootData)

    rootLeft = InputTree() # Takes left input
    rootRight = InputTree() # Takes right input

    rootNode.left = rootLeft
    rootNode.right = rootRight

    return rootNode

# Diameter is the distance between 2 farthest nodes.
# Hence, we compare the distance between left subtree's last node and right subtree's last node, versus the longest distance between 2 nodes in a single subtree
def Diameter(root):
    if root == None:
        return 0, 0
    else:
        leftHeight, leftDiameter = Diameter(root.left)
        rightHeight, rightDiameter = Diameter(root.right)

        # Return max height as well as the maximum between the different possible longest distances
        return 1 + max(leftHeight,rightHeight), max(1 + leftHeight + rightHeight, max(leftDiameter,rightDiameter)) 


root = InputTree()
printTree(root)
print("Diameter is:",Diameter(root)[1])
