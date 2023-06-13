def missingNumber(nums):
  n = len(nums)
  seen = set(nums)

  for i in range(n + 1):  
    if not i in seen: return i

print(missingNumber([3, 0, 1]))
print(missingNumber([0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))