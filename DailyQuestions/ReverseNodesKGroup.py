# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #Find length
        cur = head
        length = 0
        count = 0
        
        while cur:
            length += 1
            cur = cur.next
            
        if length == 1:
            return head
            
        cur = head
        nxt = None
        prev = None
        lst = []
        
        dummy_head = ListNode(0)
        res = ListNode(0)
        dummy_head.next = res
        
        while cur:
            if count != 0 and count%k == 0 and length - count < k:
                res.next = prev
                while res.next:
                    res = res.next
                res.next = nxt
                break
                
            elif count != 0 and count%k == 0:
                res.next = prev
                res = res.next
                
                while res.next:
                    res = res.next
                    
                cur = nxt
                nxt = None
                prev = None

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1
            
            if count == length:
                res.next = prev

        return dummy_head.next.next
