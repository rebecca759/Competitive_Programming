# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        #use bfs
        if not root:
            return
        
        queue = deque()
        result = [root.val]
        queue.append(root)
        
        while queue:
            temp = deque()
            values = []
            
            while queue:
                cur_node = queue.popleft()
                
                if cur_node.left:
                    temp.append(cur_node.left)
                    values.append(cur_node.left.val)
                    
                if cur_node.right:
                    temp.append(cur_node.right)
                    values.append(cur_node.right.val)
                
            if len(values) > 0:
                result.append(max(values))
                
            queue = temp
            
        return result
