class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        l = r = 0
        res = []
        
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
                
            queue.append(r)
            
            if r+1 >= k:
                res.append(nums[queue[0]])
                l += 1
                
            if l > queue[0]:
                queue.popleft()
                
            r += 1
            
        return res
            
        
        
        
        
        
        