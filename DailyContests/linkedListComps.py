# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cur = head
        comps = 0
        
        G = set(G)
        
        while cur:
            if cur.val in G:
                while cur:
                    if cur.val not in G:
                        break
                    cur = cur.next
   
                comps += 1
           
            if cur:
                cur = cur.next
                
            else:
                break
   
        return comps
            
                
