# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        
        result_lst = self.inorderTraversal(root,result)
        
        index = 1
        
        for node in result:
            if index == k:
                return node.val
            
            index += 1
        
    def inorderTraversal(self,root: TreeNode, result):
        if not root:
            return
    
        self.inorderTraversal(root.left,result)
        result.append(root)
        self.inorderTraversal(root.right,result)
        
        
    
        
    
