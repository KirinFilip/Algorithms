def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # while list is not empty
  while left_pointer < right_pointer:
    # calculate the middle index
    mid_index = (left_pointer + right_pointer) // 2
    mid_value = sorted_list[mid_index]

    if mid_value == target:
      return mid_index
      
    if target < mid_value:
      # if target smaller than mid value check left side of list
      # by changing the right pointer to mid index
      right_pointer = mid_index
    if target > mid_value:
      # if target bigger than mid value check right side of list
      # by changing the left pointer to mid index + 1 
      left_pointer = mid_index+1
  
  return "Value not in list"

# returns index
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))