class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morris_preorder_traversal(root):
    current = root

    while current:
        if current.left is None:
            # No left child, so we can process the current node
            print(current.val, end=" ")  # Or do whatever you want with the node value
            current = current.right  # Move to the right child
        else:
            # Find the rightmost node in the left subtree
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            if pre.right is None:
                # Make the current node the right child of its inorder predecessor
                pre.right = current
                print(current.val, end=" ")  # Or do whatever you want with the node value
                current = current.left
            else:
                # The right child of the inorder predecessor is already set (backtracking)
                pre.right = None  # Restore the tree structure
                current = current.right  # Move to the right child

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform preorder traversal using Morris algorithm
morris_preorder_traversal(root)
