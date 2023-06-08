def reverseWords(s):
  words = s.split(' ')
  for i in range(len(words) - 1, -1, -1):
    if words[i] == '':
      words.pop(i)
  left = 0
  right = len(words) - 1
  while right > left:
    aux = words[right]
    words[right] = words[left]
    words[left] = aux
    left += 1
    right -= 1

  return ' '.join(words)

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))