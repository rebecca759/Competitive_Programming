"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dic = {None:None}
        res_head = self.copy(head,copy_dic)
        ptr = res_head

        while ptr:
            ptr.random = copy_dic[head.random]
            ptr = ptr.next
            head = head.next
        
        return res_head
    
    def copy(self,node,copy_dic):
        head = Node(0)
        cur = head
        while node:
            cur.next = Node(node.val)
            copy_dic[node] = cur.next
            cur = cur.next
            node = node.next
            
        return head.next