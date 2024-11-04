def binary_search_iterative(arr: list[int], target: int) -> int:
    min_idx, max_idx = 0, len(arr) - 1
    res = -1

    while(min_idx <= max_idx):
        mid_idx = (min_idx + max_idx)//2
        if(arr[mid_idx] == target):
            return mid_idx
        elif(arr[mid_idx] < target):
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx - 1
    
    return res