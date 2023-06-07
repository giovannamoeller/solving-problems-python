def sortedSquares(nums):
  l = 0
  r = k = len(nums) - 1
  ans = [0] * (k + 1)

  while r >= l:
    if nums[l] * nums[l] > nums[r] * nums[r]:
      ans[k] = (nums[l] * nums[l])
      l += 1
    else:
      ans[k] = (nums[r] * nums[r])
      r -= 1
    k -= 1

  return ans #ans[::-1]

print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))