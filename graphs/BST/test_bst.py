from bst import BST_Node

def main():
    # insert
    root = BST_Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(25)

    assert root.val == 10
    assert root.left.val == 5
    assert root.right.val == 15
    assert root.right.right.val == 25
    
    # lookup
    assert root.lookup_val(10) == True
    assert root.lookup_val(5) == True
    assert root.lookup_val(15) == True
    assert root.lookup_val(25) == True
    assert root.lookup_val(-1) == False
    assert root.lookup_val(99) == False

    # insert_list
    root = BST_Node(15)
    root.insert_list([5, 10, 25])
    assert root.val == 15
    assert root.left.val == 5
    assert root.left.right.val == 10
    assert root.right.val == 25



if __name__ == "__main__":
    main()
