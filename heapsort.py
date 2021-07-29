from max_heap import MaxHeap

print("-----------------------")
print("HEAPSORT: O(N * log N)")
print("-----------------------")


def heapsort(lst):
  sort = []
  max_heap = MaxHeap()
  for idx in lst:
    max_heap.add(idx)
  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    sort.insert(0, max_value)
  return sort

nums = [5,9,1,3,4,6,6,3,2]
sorted_list = heapsort(nums)
print(sorted_list)