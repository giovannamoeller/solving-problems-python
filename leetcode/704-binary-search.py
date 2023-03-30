import math

def search(nums, target):
  s = 0
  e = len(nums) - 1
  while e >= s:
    m = math.floor((s + e) / 2)
    if nums[m] > target:
      e = m - 1
    elif nums[m] < target:
      s = m + 1
    else: return m
  return -1

print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))