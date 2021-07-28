# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        return self.buildBST(nums)
        
        
    def buildBST(self,nums):
        if len(nums) == 0:
            return
        
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        
        node.left = self.buildBST(nums[0:mid])
        node.right = self.buildBST(nums[mid+1:])
        
        return node
