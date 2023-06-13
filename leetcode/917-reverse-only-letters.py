def isCharacterValid(char):
  return (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)

def reverseOnlyLetters(s):
  charArr = []

  for char in s:
    charArr.append(char)

  left = 0
  right = len(charArr) - 1

  while right > left:
    if not isCharacterValid(charArr[left]):
      left += 1
      continue
    if not isCharacterValid(charArr[right]):
      right -= 1
      continue
    aux = charArr[left]
    charArr[left] = charArr[right]
    charArr[right] = aux
    left += 1
    right -= 1

  return ''.join(charArr)

print(reverseOnlyLetters("ab-cd"))
print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))