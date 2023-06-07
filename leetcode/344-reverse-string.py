def reverseString(s):
  l = 0
  r = len(s) - 1

  while r > l:
    aux = s[r]
    s[r] = s[l]
    s[l] = aux
    r -= 1
    l += 1

  return s

print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))