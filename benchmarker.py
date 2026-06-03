import time
from merge_sort import merge_sort

def benchmark_timer(func):
  # TODO: Implement the wrapper to measure time
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()

    result = func(*args, **kwargs)

    end_time = time.perf_counter()
    print(f"Elapsed: {end_time - start_time: 6f}s")
    return result
  return wrapper
  

@benchmark_timer
def run_benchmark(data):
  # TODO: Call merge_sort and return result
  return merge_sort(data)

if __name__ == "__main__":
  # Create a list of 10,000 integers to test
  large_data = list(range(10000, 0, -1)) 
  run_benchmark(large_data)