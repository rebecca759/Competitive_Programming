class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        head = result
        
        while l1 or l2:
            a = l1.val if l1 else -999
            b = l2.val if l2 else -999
            
            if a < b and a != -999:
                result.next = ListNode(a)
                l1 = l1.next
                result = result.next
                    
            elif a < b and a == -999:
                result.next = ListNode(b)
                l2 = l2.next
                result = result.next
                
            elif a > b and b != -999:
                result.next = ListNode(b)
                l2 = l2.next
                result = result.next
                    
            elif a > b and b == -999:
                result.next = ListNode(a)
                l1 = l1.next
                result = result.next
                
            elif a == b:
                result.next = ListNode(a)
                l1 = l1.next
                result = result.next
                result.next = ListNode(b)
                l2 = l2.next
                result = result.next
                
        return head.next
