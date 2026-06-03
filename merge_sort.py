def merge_sort(data):
    # Base Case: If the list is 1 or 0 elements, it's already sorted
    if # TODO: Check length of data
        return data

    # Divide: Find the midpoint and split the data
    mid = # TODO: Calculate midpoint
    left_half = # TODO: Slice data for left side
    right_half = # TODO: Slice data for right side

    # Recursive calls
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Temporary return for this lesson
    return left_sorted, right_sorted

# Test your logic
if __name__ == "__main__":
    test_list = [5, 2, 9, 1]
    print(merge_sort(test_list))