print("------------")
print("BUBBLE SORT: O(N^2)")
print("------------")

def bubble_sort_unoptimized(arr):
  iteration_count = 0
  for element in arr:
    for index in range(len(arr) - 1):
      iteration_count += 1
      if arr[index] > arr[index + 1]:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]

  print(f"PRE-OPTIMIZED ITERATION COUNT: {iteration_count}")

def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for index in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[index] > arr[index + 1]:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
        
  print(f"POST-OPTIMIZED ITERATION COUNT: {iteration_count}")


nums = [5,9,1,3,4,6,6,3,2]

print(f"UNSORTED NUMBERS: {nums}")
bubble_sort_unoptimized(nums)
bubble_sort(nums)
print(f"SORTED NUMBERS: {nums}")
