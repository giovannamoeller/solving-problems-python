def removeDuplicates(nums):
  k = 1
  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      nums[k] = nums[i]
      k += 1
  return k

print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([1, 1, 2, 3, 4, 4, 4]))