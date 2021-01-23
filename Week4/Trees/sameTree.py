# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if (not p and q) or (p and not q) or ((p and q) and p.val != q.val):
            return False
        
        elif not p and not q:
            return True
        
        elif p.val == q.val:
            s1 = self.isSameTree(p.left,q.left)
            s2 = self.isSameTree(p.right,q.right)
                
                
            return s1 and s2



    
