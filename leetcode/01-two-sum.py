def twoSum(nums, target: int):
  hashMap = {}
  for i in range(len(nums)):
    valueToBeFound = target - nums[i]
    if valueToBeFound in hashMap:
      return [hashMap[valueToBeFound], i]
    hashMap[nums[i]] = i

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))