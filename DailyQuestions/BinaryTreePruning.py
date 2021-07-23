# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        v = self.prune(root)
        
        if not v and root.val == 0:
            return
        
        return root
        
    def prune(self,node):
        if not node:
            return False
        
        if not node.left and not node.right:
            if node.val == 0:
                return False
            
            if node.val == 1:
                return True
            
        left = self.prune(node.left)  
        right = self.prune(node.right)
        
        if left == False:
            node.left = None
            
        if right == False:
            node.right = None
            
        if node.val == 1:
            return True
            
        return left or right
