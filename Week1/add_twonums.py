# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summ = 0
        carry = 0
        
        result = ListNode(0)
        head = result
        
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            result.next = ListNode(((a + b + carry) % 10) )
            carry = (a + b + carry) // 10
            
            result = result.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            result.next = ListNode(carry)
            
        return head.next


s = Solution()
#create first linked list
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next = ListNode(3)

#create second linked list
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next = ListNode(4)





