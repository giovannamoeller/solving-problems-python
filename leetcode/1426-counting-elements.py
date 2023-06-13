def countElements(arr):
  seen = set(arr)
  count = 0
  for number in arr:
    if number + 1 in seen: count += 1
  return count
    
print(countElements([1, 2, 3]))
print(countElements([1, 1, 3, 3, 5, 5, 7, 7]))