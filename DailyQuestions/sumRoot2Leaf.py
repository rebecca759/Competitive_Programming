# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        path = root.val
        
        self.dfs(root,res,path)
        
        return sum(res)
   
    def dfs(self,node,res,path):
        if not node.left and not node.right:
            res.append(path) 
            
        else:
            if node.left:
                self.dfs(node.left,res,(path*10)+node.left.val)
            if node.right:
                self.dfs(node.right,res,(path*10)+node.right.val)
            
        return res
