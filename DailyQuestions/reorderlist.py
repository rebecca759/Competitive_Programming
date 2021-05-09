# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        
        cur = head
        
        while cur:
            nodes.append(cur.val)
            cur = cur.next
            
        l = 1
        r = len(nodes)-1
        
        new = [nodes[0]]
        
        while l <= r:
            new.append(nodes[r])
            if l == r:
                break
            new.append(nodes[l])
            l += 1
            r -= 1
        
        
        _head = ListNode()
        _cur = ListNode(new[0])
        _head.next = _cur
        
        for i in range(1,len(new)):
            _cur.next = ListNode(new[i])
            _cur = _cur.next
            
            
        head.next = _head.next.next
