print("------------")
print("BIG O: N^2")
print("------------")


nums = [5,9,1,3,4,6,6,3,2]

print(f"PRE SORT: {nums}")

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
        # replacement for swap function
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
        
  print(f"POST-OPTIMIZED ITERATION COUNT: {iteration_count}")

bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print(f"POST SORT: {nums}")
