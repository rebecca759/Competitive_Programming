# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = []
        self.findleft(root,0,res)
        
        return res[-1]
        
    def findleft(self,node,level,res):
        if len(res) == level:
            res.append(node.val)
                
        if not node.left and not node.right:
            return res
        
        if node.left:
            self.findleft(node.left,level+1,res)
        if node.right:
            self.findleft(node.right,level+1,res)
        
        return res
