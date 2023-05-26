def romanToInt(s):
  romanHash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
  especialInstances = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900 }
  count = 0

  for instance in especialInstances:
    if instance in s:
      count += especialInstances[instance]
      s = s.replace(instance, "")

  for char in s:
    count += romanHash[char]
  
  return count

print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
