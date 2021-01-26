# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        if root.val >= low and root.val <= high:
            r1 = self.rangeSumBST(root.left,low,high)
            r2 = self.rangeSumBST(root.right,low,high)

            return r1 + r2 + root.val

        elif root.val > high:
            return self.rangeSumBST(root.left,low,high)

        elif root.val < low:
            return self.rangeSumBST(root.right,low,high)
