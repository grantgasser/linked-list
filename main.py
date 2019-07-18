## Driver for Linked List
## Author: Grant Gasser
## 7/17/2019

import list, node

def main():
    # create nodes
    head_node = node.Node(1)
    #nodeB = node.Node(7)
    #nodeC = node.Node(8)

    # create the list
    linked_list = list.List(head_node)

    for i in range(2,11,2):
        linked_list.push_back(i)

    # verify
    linked_list.print_list()

    # reverse
    linked_list.reverse_list()

    # verify
    linked_list.print_list()

main()
