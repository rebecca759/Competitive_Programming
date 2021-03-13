from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        averages = []
        
        queue.append((root,0))
        
        level = 0
        average = 0
        summ = 0
        count = 0
        
        
        while len(queue) > 0:
            cur_node = queue.popleft()
            
            if cur_node[1] == level:
                summ += cur_node[0].val
                count += 1
                
            else:
                average = summ/count
                averages.append(average)
                summ = 0
                count = 0
                level = cur_node[1]
                
                summ += cur_node[0].val
                count += 1
            
            if cur_node[0].left:
                queue.append((cur_node[0].left,cur_node[1]+1))
            
            if cur_node[0].right:
                queue.append((cur_node[0].right,cur_node[1]+1))
                
            average = summ/count
            
        averages.append(average)
        
        return averages
