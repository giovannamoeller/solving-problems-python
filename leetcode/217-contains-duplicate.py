def containsDuplicate(nums):
  hashNums = {}
  for i in range(len(nums)):
    if nums[i] in hashNums:
      return True
    hashNums[nums[i]] = i
  return False

print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))