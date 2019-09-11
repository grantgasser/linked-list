## BST Class
## Author: Grant Gasser
## 9/10/2019

from treenode import TreeNode

class BST():
    """
    Binary search tree of integers stored in TreeNodes
    """
    def __init__(self, root_val=None):
        """
        Just need a pointer to root node

        Args:
            root_val (int): value to be stored in root node
        """
        self.root = TreeNode(root_val)

    def insert(self, new_val):
        """
        Calls helper function and passes root and new value
        """
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        """
        Inserts new node with new value according to BST property

        Args:
            current (TreeNode): current treenode to evaluate
            new_val (int): new value to be stored in the BST
        """
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = TreeNode(new_val)

        elif current.data > new_val:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = TreeNode(new_val)

        else:
            print('Data: {}, already exists in tree!'.format(new_val))
