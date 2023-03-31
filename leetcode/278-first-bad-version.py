import math

def isBadVersion(n, bad = 4):
  return n >= bad

def firstBadVersion(n):
  s = 1
  e = n
  while e >= s:
    m = math.floor((e + s) / 2)
    if isBadVersion(m) == True and isBadVersion(m - 1) == False: return m
    elif isBadVersion(m) == False: s = m + 1
    else: e = m
  return -1

print(firstBadVersion(5))
print(firstBadVersion(1))
print(firstBadVersion(3))