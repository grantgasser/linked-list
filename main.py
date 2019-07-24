## Driver for Linked List
## Author: Grant Gasser
## 7/17/2019

import list, node, treenode

def main():
    # create nodes
    head_node = node.Node(1)
    #nodeB = node.Node(7)
    #nodeC = node.Node(8)

    # create the list
    linked_list = list.List(head_node)

    for i in range(2,11,2):
        linked_list.append(i)

    # verify
    linked_list.print_list()

    # reverse
    print('\nReversing list...\n')
    linked_list.reverse_list_iterative()

    # verify
    linked_list.print_list()

    # reverse
    print('\nReversing list...\n')
    linked_list.reverse_list_recursive(linked_list.get_head())

    # verify
    linked_list.print_list()



    #### BST Testing ####

    # Test creation tree node
    root = treenode.TreeNode(5)

    print('\nExpecting 5:', root.get_data())

    # Test get child functions
    print('\nExpecting None:', root.get_left_child())
    print('Expecting None:', root.get_right_child())


main()
