## Linked List Class
## Author: Grant Gasser
## 7/17/2019

import node

class List():
    def __init__(self, head=None):
        """
        A linked list object need only consist of pointer to head node
        """
        self.head = head

    def push_back(self, data):
        """
        Push node with new data to the back of the linked list

        Args:
            data (int): data for a node to be added at end of list

        Returns:
            self: reference to itself for chaining
        """
        new_node = node.Node(data)

        if not self.head:
            self.head = new_node

        else:
            temp = self.head

            while(temp.next):
                temp = temp.next

            temp.next = new_node


        return self


    def reverse_list(self):
        """
        Reverse the direction of the arrows in the list. O(2N) solution.
        """
        pass



    def print_list(self):
        """
        Iterate through a print data of each node from list (start at head)
        """

        temp = self.head

        while(temp):
            print(temp)
            temp = temp.next
