from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        elif self.isLeaf(root):
            return 1
        
        else:
            return self._minDepth(root)
          
    def _minDepth(self, root):
        queue = deque()
        level = 1
        queue.appendleft((root,level))
        
        while len(queue) > 0:
            node = queue.pop()
            
            if node[0].left:
                queue.appendleft((node[0].left,node[1]+1))
                
            if node[0].right:
                queue.appendleft((node[0].right,node[1]+1))
                
            if self.isLeaf(node[0]):
                return node[1]
        
    def isLeaf(self,node):
        return (node.left == None) and (node.right == None)
        
