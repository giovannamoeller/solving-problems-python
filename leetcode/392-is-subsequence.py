def isSubsequence(s, t):
  if len(s) > len(t): return False
  i = j = 0
  while i < len(s) and j < len(t):
    if s[i] == t[j]:
      i += 1
    j += 1

  return i == len(s)

    
print(isSubsequence('abc', 'ahbgdc'))
print(isSubsequence('axc', 'ahbgdc'))