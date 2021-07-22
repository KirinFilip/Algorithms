print("-------------------------")
print("MERGE SORT: O(N * log N)")
print("-------------------------")

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2

  left_sorted = merge_sort(items[:middle_index])
  right_sorted = merge_sort(items[middle_index:])

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result


nums = [5,9,1,3,4,6,6,3,2]
print(f"UNSORTED NUMBERS: {nums}")
print(f"SORTED NUMBERS: {merge_sort(nums)}")