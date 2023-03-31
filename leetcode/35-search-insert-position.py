import math

def searchInsert(nums, target):
  s = 0
  e = len(nums) - 1
  while e >= s:
    m = math.floor((e + s) / 2)
    if nums[m] > target: e = m - 1
    elif nums[m] < target: s = m + 1
    else: return m
  return e + 1

print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))