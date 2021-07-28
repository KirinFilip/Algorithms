def binary_search(sorted_list, left_pointer, right_pointer, target):
  # check if sorted_list is empty
  if not sorted_list:
    return "value not found"
	
  # calculate the middle index
  mid_index = (left_pointer + right_pointer) // 2
  mid_value = sorted_list[mid_index]

  # base case
  if mid_value == target:
    return mid_index

  if mid_value > target:
    # recursively check the left side of the list
    # reduce the sub-list by passing in a new right_pointer
    return binary_search(sorted_list, left_pointer, mid_index, target)
    
  if mid_value < target:
    # recursively check the right side of the list
    # reduce the sub-list by passing in a new left_pointer
    return binary_search(sorted_list, mid_index + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
target = 288
result = binary_search(values, start_of_values, end_of_values, target)

print(f"element {target} is located at index {result}")