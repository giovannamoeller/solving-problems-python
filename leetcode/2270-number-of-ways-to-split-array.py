def waysToSplitArray(nums):
  left_section = ans = 0
  total = sum(nums)

  for i in range(len(nums) - 1):
    left_section += nums[i]
    right_section = total - left_section
    if left_section >= right_section:
      ans += 1

  return ans

print(waysToSplitArray([10, 4, -8, 7]))