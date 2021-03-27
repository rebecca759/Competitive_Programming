# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        temp = root.left 
        root.left = root.right
        root.right = temp
            
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


#Using BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #Using BFS
        
        if not root:
            return
        
        q = deque()
        
        q.append(root)
        
        while q:
            cur_root = q.popleft()
            
            temp = cur_root.left
            cur_root.left = cur_root.right
            cur_root.right = temp
            
            if cur_root.left:
                q.append(cur_root.left)
                
            if cur_root.right:
                q.append(cur_root.right)
                
            
        return root
