# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        right_sum = 0
        left_sum = 0
        
        if not root:
            return False
        
        summ = root.val
        
        if not root.left and not root.right:
            if targetSum == summ:
                return True
            else:
                return False
            
        left_sum = self.dfs(root.left,targetSum,summ)
        right_sum = self.dfs(root.right,targetSum,summ)
            
        if not root.right:
            right_sum = False
        
        elif not root.left:
            left_sum = False
            
            
        return left_sum or right_sum

    def dfs(self,node,targetSum,summ):
        if not node:
            return False
        
        summ += node.val
        
        if summ == targetSum and not node.left and not node.right:
            return True
        
        left = self.dfs(node.left,targetSum,summ)
        right = self.dfs(node.right,targetSum,summ)

        
        if left:
            return True
        
        else:
            return right
