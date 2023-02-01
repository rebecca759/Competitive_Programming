# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        
        mid = len(nums)//2
        cur_root = TreeNode(nums[mid])
        cur_root.left = self.sortedArrayToBST(nums[:mid])
        cur_root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return cur_root