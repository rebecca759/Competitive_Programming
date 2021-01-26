# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        else:
            return self.symmetric(root.left,root.right);
    
        
    def symmetric(self,left,right):
        if not left and not right:
            return True
        
        elif (not left and right) or (not right and left) or (right and left and right.val != left.val):
            return False
        
        if (left and right and left.val == right.val):
            val1 = self.symmetric(left.left,right.right)
            val2 = self.symmetric(left.right,right.left)
            
            return val1 and val2
        
        
