# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = self.length(head)
        k = k%length
        if k == 0:
            return head
        
        fast = head
        slow = head
        
        while k > 0:
            fast = fast.next
            k -= 1
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            
        first = slow.next
        slow.next = None
        fast.next = head
        
        return first
        
    
    def length(self,node):
        tot = 0
        
        while node:
            tot += 1
            node = node.next
            
        return tot