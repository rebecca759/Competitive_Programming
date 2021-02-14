# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 0
        
        return self.dfs(root.left,root) + self.dfs(root.right,root)
            
            
    def dfs(self,node, parent):
        left = 0
        right = 0
        
        if not node:
            return 0
        
        if (parent.val % 2 == 0):
            if node.left:
                left = node.left.val
                
            if node.right:
                right = node.right.val
                
        return left + right + self.dfs(node.left,node) + self.dfs(node.right,node)
            
