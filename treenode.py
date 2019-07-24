## Tree Node Class
## Author: Grant Gasser
## 7/17/2019

from node import Node

class TreeNode(Node):
    """
    A TreeNode class for binary search tree. Inherits from Node class.
    """
    def __init__(self, data=-1, left=None, right=None):
        """
        Each node has a left and right child

        Args:
            data (int): the data to be stored in node
            left (Node): a pointer to the left child
            right (Node): a pointer to the right child
        """
        self.left = left
        self.right = right

        Node.__init__(self, data)



    def get_data(self):
        """
        Returns data
        """
        return self.data

    def get_left_child(self):
        """
        Returns left child
        """
        return self.left


    def get_right_child(self):
        """
        Returns right child
        """
        return self.left
