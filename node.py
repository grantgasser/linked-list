## Node Class
## Author: Grant Gasser
## Date: 7/17/2019


# Define a Node
class Node:
    """
    Each node has a value and pointer to next node (not doubly for now)
    """
    def __init__(self, data):
        """
        A class to represent a node in a linked list

        Args:
            data (int): the data to be stored in node
            next (Node): a pointer to the next node in the list
        """
        self.data = data
        self.next = None


    def get_data(self):
        """
        Returns data
        """
        return self.data


    def __str__(self):
        """
        Overloading magic method. Turn object into printable string.
        """
        return str(self.data) 

    def __repr__(self):
        """
        Overloading magic method. Determine what to print when object typed
        into interpreter.
        """
        return str(self.data)
