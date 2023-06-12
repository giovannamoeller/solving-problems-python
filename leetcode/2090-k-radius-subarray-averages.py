import math
#floor

def getAverages(nums, k):
  prefix = [nums[0]]
  avgs = []
  j = 0

  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[j])
    j += 1

  for i in range(len(nums)):
    if i < k or len(nums) - i <= k:
      avgs.append(-1)
    else:
      sum = prefix[i + k] - prefix[i - k] + nums[i - k]
      length = i + k - (i - k) + 1
      avgs.append(math.floor(sum / length))

  return avgs

print(getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
print(getAverages([8], 1000))
  