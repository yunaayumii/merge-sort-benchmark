def bubble_sort(data):
  # Work on a copy to keep the original data intact
  n = len(data)
  arr = list(data)
  
  for i in range(n):
    # Last i eltements are already in place
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+ 1] = arr[j + 1], arr[j]
          
  return arr

if __name__ == "__main__":
  test_list = [5, 2, 9, 1]
  print(f"Naive Sort Result: {bubble_sort(test_list)}")