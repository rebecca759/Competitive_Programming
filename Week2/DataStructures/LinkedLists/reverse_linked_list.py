class Solution:
    def __init__(self):
        self.result = None
        
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        if not head.next:
            self.result = head
            return self.result
            
        res = self.reverseList(head.next)
        q = head.next
        q.next = head
        head.next = None
        
        return self.result

#Recursively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        if not head.next:
            return head

        #keep adding to call stack until last element
        result = self.reverseList(head.next)
        #At this point we're going upwards in the call stack b/c we've finished last call
        #reverse
        head.next.next = head
        #break the cycle
        head.next = None

        return result
