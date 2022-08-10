# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head
        res_head = cur_head = ListNode(0)
        
        while cur:
            temp = cur.next.next if cur.next else None
            if cur.next:
                cur.next.next = None 
                
            else:
                cur_head.next = cur
                break
            
            cur_head.next = cur.next
            cur_head = cur_head.next
            cur.next = None
            cur_head.next = cur
            cur_head = cur_head.next 
            cur = temp
        
        return res_head.next