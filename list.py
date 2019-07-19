## Linked List Class
## Author: Grant Gasser
## 7/17/2019

import node

class List():
    def __init__(self, head=None):
        """
        A linked list object need only consist of pointer to head node.
        """
        self._head = head

    def get_head(self):
        return self._head

    def push_back(self, data):
        """
        Push node with new data to the back of the linked list

        Args:
            data (int): data for a node to be added at end of list

        Returns:
            self: reference to itself for chaining
        """
        new_node = node.Node(data)

        if not self._head:
            self._head = new_node

        else:
            temp = self._head

            while(temp.next):
                temp = temp.next

            temp.next = new_node


        return self


    def reverse_list_iterative(self):
        """
        Reverse the direction of the arrows in the list. Iterative solution with
        three pointers: prev, curr, next. Time Complexity: O(N)
        """
        prev = None
        curr = self._head
        next = None

        # reverse the list until curr is None
        while curr:
            # swap
            next = curr.next
            curr.next = prev

            # move forward
            prev = curr
            curr = next


        #set head to last (now first) node
        self._head = prev


    def reverse_list_recursive(self, curr, prev=None, next=None):
        """
        Reverse the direction of the arrows in the list. Recursive solution with
        three pointers: prev, curr, next. Time Complexity: O(N)
        """
        if not curr: # base case, at the end of the list
            self._head = prev
        else:
            next = curr.next
            curr.next = prev

            # recursive call
            self.reverse_list_recursive(next, curr)



    def print_list(self):
        """
        Iterate through a print data of each node from list (start at head)
        """

        temp = self._head

        while(temp):
            print(temp)
            temp = temp.next
