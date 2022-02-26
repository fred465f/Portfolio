# Linear Search Algorithm - looks for all instances of target_value,
# if instances is found, it returns their index's, else it raises
# a value error. Runs in O(n) time complexity for list of n elements.
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))