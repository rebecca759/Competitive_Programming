# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        current = node
        current_val = node.val
        
        while current.next:
            prev = current
            current = current.next
            temp = current.val
            current.val = current_val
            prev.val = temp
            
        prev.next = None
