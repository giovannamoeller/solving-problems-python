def isAnagram(s, t):
  hashMap = {}

  if len(s) != len(t): return False

  for char in s:
    if char in hashMap: hashMap[char] += 1
    else: hashMap[char] = 1

  for char in t:
    if char not in hashMap or hashMap[char] == 0:
      return False
    else:
      hashMap[char] -= 1
  return True

print(isAnagram('anagram', 'nagaram'))
print(isAnagram('rat', 'car'))
print(isAnagram('a', 'ab'))
print(isAnagram('aacc', 'ccac'))