def runningSum(nums):
  runningSum = [nums[0]]
  j = 0
  for i in range(1, len(nums)):
    currentSum = nums[i] + runningSum[j]
    runningSum.append(currentSum)
    j += 1
  return runningSum

print(runningSum([1, 1, 1, 1, 1]))
print(runningSum([1, 2, 3, 4]))
print(runningSum([3, 1, 2, 10, 1]))