# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = head
        prev = None
        
        if not head:
            return
            
        elif head.val == val and not head.next:
            return
        
        while current:
            if head.val == val and head.next:
                head.val, head.next.val = head.next.val,head.val
                head.next = head.next.next
                prev = head
                
            elif current.val == val:
                prev.next = current.next
                current = current.next   
                
            else:
                prev = current
                current = current.next

                
        if head.val == val:
            return 
      

        return head
        
