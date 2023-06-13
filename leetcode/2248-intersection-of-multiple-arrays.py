def intersection(nums):
  hashMap = {}
  ans = []
  for list in nums:
    for x in list:
      if x in hashMap: hashMap[x] += 1
      else: hashMap[x] = 1
  
  for key in hashMap:
    if hashMap[key] == len(nums): ans.append(key)
  
  return sorted(ans)

print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(intersection([[1,2,3],[4,5,6]]))