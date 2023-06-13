def moveZeroes(nums):
  i = j = 0
  while i < len(nums) and j < len(nums):
    if nums[i] == 0:
      i += 1
    else:
      aux = nums[i]
      nums[i] = nums[j]
      nums[j] = aux
      j += 1
      i += 1
  print(nums)
      
moveZeroes([0, 1, 0, 3, 12])
moveZeroes([0])