def isValid(s):
  stack = []
  openClosingHash = {
    ')': '(',
    '}': '{',
    ']': '['
  }

  for char in s:
    if char in openClosingHash:
      if len(stack) != 0 and stack[-1] == openClosingHash[char]: 
        stack.pop()
      else:
        return False
    else:
      stack.append(char)

  return len(stack) == 0

print(isValid('()'))
print(isValid("()[]{}"))
print(isValid('(]'))
print(isValid('(]['))
print(isValid('(][)'))