def mergeAlternately(word1, word2):
  mergedStrs = ''
  i = j = 0

  while i < len(word1) and j < len(word2):
    mergedStrs += word1[i]
    mergedStrs += word2[j]
    i += 1
    j += 1

  while i < len(word1):
    mergedStrs += word1[i]
    i += 1

  while j < len(word2):
    mergedStrs += word2[j]
    j += 1

  return mergedStrs

print(mergeAlternately('abc', 'pqr'))
print(mergeAlternately('ab', 'pqrs'))
  