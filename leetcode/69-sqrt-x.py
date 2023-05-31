import math

def mySqrt(x):
  start = 0
  end = x
  res = 0
  while end >= start:
    mid = math.ceil((start + end) / 2)
    if (mid * mid) > x:
      end = mid - 1
    elif (mid * mid) < x:
      start = mid + 1
      res = mid
    else: return mid
  return res

print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(9))
print(mySqrt(10))
print(mySqrt(36))
print(mySqrt(2147395599))