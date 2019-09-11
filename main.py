## Driver for Linked List
## Author: Grant Gasser
## 7/17/2019

import list, node, treenode, bst

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

    #### TreeNode Testing ####

    # Test creation tree node
    test_node = treenode.TreeNode(5, 2, 3)

    print('\nExpecting 5:', test_node.get_data())

    # Test get child functions
    print('\nExpecting 2:', test_node.get_left_child())
    print('Expecting 3:', test_node.get_right_child())


    #### BST Testing ####
    tree = bst.BST(8)

    print('\nTEST BST')
    print('Expect 8:', tree.root.data)

    tree.insert(11)
    tree.insert(3)
    tree.insert(14)
    tree.insert(9)

    print('\nTEST INSERT BST')
    print('Expect 11:', tree.root.right.data)
    print('Expect 3:', tree.root.left.data)
    print('Expect 14:', tree.root.right.right.data)
    print('Expect 9:', tree.root.right.left.data)


main()
