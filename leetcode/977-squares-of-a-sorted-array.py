def sortedSquares(nums):
  s = 0
  e = len(nums) - 1
  squaredArr = []
  while s <= e:
    if nums[s] * nums[s] > nums[e] * nums[e]:
      squaredArr.append(nums[s] * nums[s])
      s += 1
    else:
      squaredArr.append(nums[e] * nums[e])
      e -= 1
  squaredArr.reverse()
  return squaredArr #squaredArr[::-1]

print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))