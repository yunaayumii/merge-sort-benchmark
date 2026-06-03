def merge(left: list, right: list):
	merged = []
	# todo: while loop to compare elements
	while len(left) > 0 and len(right) > 0: 
		if left[0] <= right[0]:
			merged.append(left.pop(0))
		else:
			merged.append(right.pop(0))
	return merged
		
	# todo: handle remainig elements in left or right
	merged.extend(left)
	merged.extend(right)

def merge_sort(data: list):
	if len(data) <= 1:
		return data

	mid = len(data) // 2
	left_half = data[:mid]
	right_half = data[mid:]

	left_sorted = merge_sort(left_half)
	right_sorted = merge_sort(right_half)

	#replace with merge() helper
	return merge(left_sorted, right_sorted)

# Test your logic
if __name__ == "__main__":
	test_list = [5, 2, 9, 1]
	print(merge_sort(test_list))