def bubble_sort(data):
    # Work on a copy to keep the original data intact
    n = len(data)
    arr = list(data)
    
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, # TODO: Complete the range):
            # TODO: If current element is greater than the next, swap them
            pass
            
    return arr

if __name__ == "__main__":
    test_list = [5, 2, 9, 1]
    print(f"Naive Sort Result: {bubble_sort(test_list)}")