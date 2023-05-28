class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

def mergeTwoLists(list1, list2):
  head = sortedList = ListNode()

  while list1 and list2:
    if list1.val < list2.val:
      sortedList.next = list1
      list1 = list1.next
    else:
      sortedList.next = list2
      list2 = list2.next
    sortedList = sortedList.next
        
  if list1:
    sortedList.next = list1
  if list2:
    sortedList.next = list2

 # while head:
    #print(head.val, end=' ')
    #head = head.next
  
  return head.next

list01 = ListNode(1)
list01.next = ListNode(2) 
list01.next.next = ListNode(4)

list02 = ListNode(1)
list02.next = ListNode(3)
list02.next.next = ListNode(4)

print(mergeTwoLists(list01, list02))