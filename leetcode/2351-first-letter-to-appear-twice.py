def repeatedCharacter(s):
  charSet = set()

  for i in range(len(s)):
    if s[i] in charSet: return s[i]
    charSet.add(s[i])

print(repeatedCharacter('abccbaacz'))
print(repeatedCharacter('abcdd'))