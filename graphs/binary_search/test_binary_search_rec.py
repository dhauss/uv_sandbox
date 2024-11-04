from binary_search import binary_search_recursive

def main():
    test_1 = [1, 2, 3]
    test_2 = [1, 2]
    test_3 = []
    test_4 = [1]

    assert binary_search_recursive(test_1, 0, 0, len(test_1) - 1) == -1
    assert binary_search_recursive(test_1, 1, 0, len(test_1) - 1) == 0
    assert binary_search_recursive(test_1, 2, 0, len(test_1) - 1) == 1
    assert binary_search_recursive(test_1, 3, 0, len(test_1) - 1) == 2

    assert binary_search_recursive(test_2, 1, 0, len(test_2) - 1) == 0
    assert binary_search_recursive(test_2, 2, 0, len(test_2) - 1) == 1

    assert binary_search_recursive(test_3, 0,  0, len(test_3) - 1) == -1
    
    assert binary_search_recursive(test_4, 1, 0, len(test_4) - 1) == 0

if __name__ == '__main__':
    main()
