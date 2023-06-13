def reverseWords(s):
  #return " ".join([x[::-1] for x in s.split()])
  charArr = []
  for char in s:
    charArr.append(char)
  left = right = 0
  for i in range(len(charArr)):
    if charArr[i] == ' ' or i == len(charArr) - 1:
      right = i - 1 if charArr[i] == ' ' else i
      while right > left:
        aux = charArr[left]
        charArr[left] = charArr[right]
        charArr[right] = aux
        right -= 1
        left += 1
      left = i + 1
  return ''.join(charArr)
    
print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))