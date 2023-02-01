# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root,-float('inf'),float('inf'))
    
    def is_valid(self,node,left_bound,right_bound):
        if not node:
            return True
        
        elif node.val >= right_bound or node.val <= left_bound:
            return False
        
        return self.is_valid(node.left,left_bound,node.val) and self.is_valid(node.right,node.val,right_bound)
    