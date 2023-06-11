def minStartValue(nums):
  prefix = [nums[0]]
  j = ans = 0

  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[j])
    j += 1

  for i in range(len(prefix)):
    if prefix[i] < ans:
      ans = prefix[i]

  return 1 - (ans)
  
print(minStartValue([-3, 2, -3, 4, 2]))
print(minStartValue([1, 2]))
print(minStartValue([1, -2, -3]))