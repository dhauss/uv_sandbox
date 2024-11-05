import pytest

from bst import BST_Node

@pytest.fixture
def bst_insert():
    root = BST_Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(25)

    return root

@pytest.fixture
def bst_insert_list():
    root = BST_Node(15)
    root.insert_list([5, 10, 25])

    return root

@pytest.fixture
def bst_single_node():
    return BST_Node(10)

@pytest.fixture
def bst_empty():
    return BST_Node()

def test_insert(bst_insert):
    assert bst_insert.val == 10
    assert bst_insert.left.val == 5
    assert bst_insert.right.val == 15
    assert bst_insert.right.right.val == 25

def test_insert_list(bst_insert_list):
    assert bst_insert_list.val == 15
    assert bst_insert_list.left.val == 5
    assert bst_insert_list.left.right.val == 10
    assert bst_insert_list.right.val == 25

def test_duplicate_insert(bst_single_node):
    bst_single_node.insert(10)

    assert bst_single_node.val == 10
    assert not bst_single_node.left.val
    assert not bst_single_node.right.val

def test_lookup(bst_insert_list):
    assert bst_insert_list.lookup_val(10)
    assert bst_insert_list.lookup_val(5)
    assert bst_insert_list.lookup_val(15)
    assert bst_insert_list.lookup_val(25)
    assert not bst_insert_list.lookup_val(-1)
    assert not bst_insert_list.lookup_val(99)

def test_min_val(bst_insert, bst_insert_list, bst_single_node, bst_empty, bst_none):
    assert bst_insert.min_val() == 5
    assert bst_insert_list.min_val() == 5
    assert bst_single_node.min_val() == 10
    assert not bst_empty.min_val()
