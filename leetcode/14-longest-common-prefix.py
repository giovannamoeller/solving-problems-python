def longestCommonPrefix(strs):
  if len(strs) == 0: return ""
  prefix = strs[0]

  for i in range(1, len(strs)):
    while strs[i].find(prefix) != 0:
      prefix = prefix[:-1]

  return prefix

print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['reflower', 'flow', 'flight']))
print(longestCommonPrefix(['dog', 'racecar', 'car']))
print(longestCommonPrefix(['c', 'acc', 'ccc']))