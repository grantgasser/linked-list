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

    # create list [1,2,4,6,8,10]
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

    # test get_position
    print('\nExpecting 6:', linked_list.get_position(4))

    # test insert
    linked_list.insert(99, 3)
    print('\nExpecting 1,2,99,4,6,8,10:')
    linked_list.print_list()

    # test insert at position end
    linked_list.insert(55, 8)
    print('\nExpecting 1,2,99,4,6,8,10,55:')
    linked_list.print_list()

    # test insert out of bounds
    linked_list.insert(21, 10) # expect error message

    # test delete
    linked_list.delete(99)
    print('\nExpecting 1,2,4,6,8,10,55:')
    linked_list.print_list()

    #### BST Testing ####

    # Test creation tree node
    root = treenode.TreeNode(5)

    print('\nExpecting 5:', root.get_data())

    # Test get child functions
    print('\nExpecting None:', root.get_left_child())
    print('Expecting None:', root.get_right_child())


main()
