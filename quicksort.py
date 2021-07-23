print("--------------------------")
print("QUICKSORT SORT:")
print("Average case: O(N * log N)")
print("Worst case: O(N^2)")
print("--------------------------")

from random import randrange # randrange used to pick a random index

def quicksort(list, start, end):
  # base case - when the list from start to end contains one or zero elements,
  # when the start pointer is greater than or equal to the end pointer 
  if start >= end:
    return

  # select random element to be the pivot element
  pivot_index = randrange(start, end+1)
  pivot_element = list[pivot_index]
  # swap pivot element with last element in sub-list
  # that way we know where the pivot element is located
  list[end], list[pivot_index] = list[pivot_index], list[end]

  # PARTITIONING:
  # tracks all elements which should be to left (lesser than) of pivot element
  less_than_pointer = start

  for index in range(start, end):
    # if we found an element out of place
    if list[index] < pivot_element:
      # swap element at index with the element at less_than_pointer
      list[index], list[less_than_pointer] = list[less_than_pointer], list[index]
      # move less_than_pointer for one to the right (closer to pivot element)
      less_than_pointer += 1
  # when finished, move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  # RECURSION:
  # Call quicksort on the "left" and "right" sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)
  
  
nums = [5,9,1,3,4,6,6,3,2]
print(f"UNSORTED NUMBERS: {nums}")
quicksort(nums, 0, len(nums)-1)
print(f"SORTED NUMBERS: {nums}")
