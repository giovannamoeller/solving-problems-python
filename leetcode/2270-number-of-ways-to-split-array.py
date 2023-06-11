def waysToSplitArray(nums):
  prefix = [nums[0]]
  j = ans = 0

  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[j])
    j += 1

  for i in range(len(nums) - 1):
    left_section = prefix[i]
    right_section = prefix[len(prefix) - 1] - prefix[i]
    if left_section >= right_section:
      ans += 1

  return ans

print(waysToSplitArray([10, 4, -8, 7]))