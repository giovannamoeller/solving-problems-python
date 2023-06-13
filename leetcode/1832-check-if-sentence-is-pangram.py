def checkIfPangram(sentence):
  seen = set(sentence)
  return len(seen) == 26

print(checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))
print(checkIfPangram('leetcode'))
  