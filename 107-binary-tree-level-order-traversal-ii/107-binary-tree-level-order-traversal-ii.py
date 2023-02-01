# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        q = deque([root])
        res = []
        
        while q:
            temp = deque()
            res.append([])
            while q:
                cur = q.popleft()
                res[-1].append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                    
            q = temp
            
        return res[::-1]
        
        