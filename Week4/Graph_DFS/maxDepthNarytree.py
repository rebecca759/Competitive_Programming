"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_childn = 0

        if not root.children:
            return 1
        
        for node in root.children:
            val = self.maxDepth(node)
            max_childn = max(max_childn,val)
            
        return max_childn + 1
