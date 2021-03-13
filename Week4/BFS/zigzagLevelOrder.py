# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        queue = deque()
        result = []
        switch = True
        
        if not root:
            return result
        
        queue.append(root)
        result.append([root.val])
        
        while len(queue) > 0:
            tempQueue = deque()
            temp_result = []
            
            while len(queue) > 0:
                cur_node = queue.popleft()
                
                if cur_node.left:
                    tempQueue.append(cur_node.left)
                    
                if cur_node.right:
                    tempQueue.append(cur_node.right)
                    
            queue = tempQueue
            
            if switch:
                for i in range(len(queue)-1,-1,-1):
                    temp_result.append(queue[i].val)
                
            else:
                for i in range(len(queue)):
                    temp_result.append(queue[i].val)
                    
            switch = not(switch)
            
            if len(temp_result) > 0:
                result.append(temp_result)
            
        return result
                
            
            
