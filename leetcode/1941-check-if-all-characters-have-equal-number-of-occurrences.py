def areOccurrencesEqual(s):
  hash = {}
  for c in s:
    if not c in hash: hash[c] = 1
    else: hash[c] += 1
  return len(set(hash.values())) == 1
    
print(areOccurrencesEqual('abacbc'))
print(areOccurrencesEqual('aaabb'))