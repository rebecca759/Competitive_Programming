# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        size = 0
        index = 0
        
        while current:
            size += 1
            current = current.next
      
        current = head
        index = 0
        middle = (size // 2) 
        
        while current:
            if index == middle:
                return current
            current = current.next
            index += 1
