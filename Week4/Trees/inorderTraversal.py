# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode):
        return self.inorder(root,[])
        
        
    def inorder(self,root,result):
        if not root:
            return 
        
        self.inorder(root.left,result)
        result.append(root.val)
        self.inorder(root.right,result)
            
        return result

s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print(s.inorderTraversal(root))
