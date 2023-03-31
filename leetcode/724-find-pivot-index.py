def pivotIndex(nums):
  left = 0
  right = sum(nums)
  for i in range(len(nums)):
    right -= nums[i]
    if left == right: return i
    left += nums[i]
  return -1

print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
print(pivotIndex([2, 1, -1]))