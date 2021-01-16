# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        head = result
        
        while l1 and l2:
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
                result = result.next
                
            elif l1.val > l2.val:
                result.next = l2
                l2 = l2.next
                result = result.next
                    
        result.next = l1 if l1 else l2
                
        return head.next
