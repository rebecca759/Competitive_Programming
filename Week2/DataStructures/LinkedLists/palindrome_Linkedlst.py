# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        array = []

        while current:
            array.append(current.val)
            current = current.next
            
        i = 0
        j = len(array)-1
        
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j-= 1
        
        return True

#O(n) time constant space?
