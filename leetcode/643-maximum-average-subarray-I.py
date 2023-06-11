def findMaxAverage(nums, k):
  curr = ans = 0

  for i in range(k):
    curr += nums[i]

  ans = curr

  for i in range(k, len(nums)):
    curr += nums[i] - nums[i - k]
    ans = max(ans, curr)

  return ans / k

print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))