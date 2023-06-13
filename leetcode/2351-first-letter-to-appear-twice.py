def repeatedCharacter(s):
  charSet = set()

  for c in s:
    if c in charSet: return c
    charSet.add(c)

print(repeatedCharacter('abccbaacz'))
print(repeatedCharacter('abcdd'))