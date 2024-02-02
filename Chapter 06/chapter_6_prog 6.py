COUNT = [5] #spaces away from previous layer

# Binary Search Tree
class BSTree:
    # Function to insert a new node with given data
    def insert(self, root, val):
        # check for empty tree
        if root is None:
            return newNode(val)
        else:
            # If given val is less than root val, then find in left subtree
            if val < root.val:
                root.left = self.insert(root.left, val)
            # If given val is more than root val, then find in right subtree
            else:
                root.right = self.insert(root.right, val)
            return root

    # Search a given val in BST
    def search(self, root, val):
        # Base case
        if root is None or root.val == val:
            return root
        # If given val is less than root's val, then it lies in left subtree
        if root.val > val:
            return self.search(root.left, val)
        # If given val is more than root's val, then it lies in right subtree
        return self.search(root.right, val)

    # Delete a node from BST
    def delete(self, root, val):
        # Base case
        if root is None:
            return root
        # If given val is less than root's val, then it lies in left subtree
        if val < root.val:
            root.left = self.delete(root.left, val)
        # If given val is more than root's val, then it lies in right subtree
        elif val > root.val:
            root.right = self.delete(root.right, val)
        # If current node is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children
            # Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(root.right)
            # Copy the inorder successor's content to this node
            root.val = temp.val
            # Delete the inorder successor
            root.right = self.delete(root.right, temp.val)
        return root

    # Helper function to find the smallest node in the given tree
    def minValueNode(self, node):
        current = node
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left
        return current

# Binary Tree Node: Create a new Node
class newNode:
    # __init__ functions to create a newNode
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Function to print binary tree in 2D
# It does reverse inorder traversal
def printTreeUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    printTreeUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    printTreeUtil(root.left, space)

# Wrapper over print2DUtil()
def printTree(root):
    # Pass initial space count as 0
    printTreeUtil(root, 0)

# Driver Code
if __name__ == '__main__':
    bst = BSTree()
    root = None
    root = bst.insert(root, 10)
    root = bst.insert(root, 8)
    root = bst.insert(root, 15)
    root = bst.insert(root, 6)
    root = bst.insert(root, 9)
    root = bst.insert(root, 12)
    root = bst.insert(root, 17)
    root = bst.insert(root, 14)
    root = bst.delete(root, 8)
    printTree(root)