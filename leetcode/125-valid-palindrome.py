def isPalindrome(s):

  nonAlphabetical = ['@', ' ', ',', '.', ':', ';', '!', '#', '$', '%', '_', '"', "'", '\\', '/', '-', '{', '}', '(', ')','[', ']', '?', '`']

  for x in nonAlphabetical:
    s = s.replace(x, '')
  s = s.lower()

  l = 0
  r = len(s) - 1

  while r > l:
    if s[l] != s[r]: return False
    r -= 1
    l += 1
  
  return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))