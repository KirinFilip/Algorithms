print("--------------------")
print("LINEAR SEARCH: O(N)")
print("--------------------")

def linear_search(lst, value):
  matches = []
  for i in range(len(lst)):
    if lst[i] == value:
      matches.append(i)
  if matches:
    return matches
  else:
    raise ValueError(f"{value} not in list")

locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target = "New York City"
print(linear_search(locations, target))


def linear_search(lst):
  max_score_index = None
  for i in range(len(lst)):
    if max_score_index == None or lst[i] > lst[max_score_index]:
      max_score_index = i
  return max_score_index

test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
print(linear_search(test_scores))