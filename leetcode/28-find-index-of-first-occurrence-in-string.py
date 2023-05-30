def strStr(haystack, needle):
  #return haystack.find(needle)
  if len(needle) > len(haystack): 
    return -1
  
  j = 0

  while j < len(haystack):
    if haystack[j:len(needle) + j] == needle:
      return j
    j += 1

  return -1

print(strStr("mississippi", "issi"))
print(strStr("leetcode", "leeto"))
print(strStr("leetcode", "co"))
print(strStr("aaaaa", "bba"))
print(strStr("aaa", "aaaa"))
print(strStr("mississipi", "issipi"))



