from binary_search import binary_search_iterative

def main():
    test_1 = [1, 2, 3]
    test_2 = [1, 2]
    test_3 = []
    test_4 = [1]

    assert binary_search_iterative(test_1, 0) == -1
    assert binary_search_iterative(test_1, 1) == 0
    assert binary_search_iterative(test_1, 2) == 1
    assert binary_search_iterative(test_1, 3) == 2

    assert binary_search_iterative(test_2, 1) == 0
    assert binary_search_iterative(test_2, 2) == 1

    assert binary_search_iterative(test_3, 0) == -1
    
    assert binary_search_iterative(test_4, 1) == 0

if __name__ == '__main__':
    main()
