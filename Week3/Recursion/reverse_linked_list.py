#Iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
   
        return prev

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
