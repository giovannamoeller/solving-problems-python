def runningSum(nums):
  prefix = [nums[0]]
  j = 0

  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[j])
    j += 1

  return prefix

print(runningSum([1, 1, 1, 1, 1]))
print(runningSum([1, 2, 3, 4]))
print(runningSum([3, 1, 2, 10, 1]))