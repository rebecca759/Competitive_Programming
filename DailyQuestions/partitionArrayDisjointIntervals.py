class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_length = 1
        max_in_left = nums[0]
        max_so_far = nums[0]
        
        for i in range(1,len(nums)):  
            max_so_far = max(max_so_far,nums[i])
            
            if nums[i] < max_in_left:
                left_length = i+1
                max_in_left = max_so_far
                
        return left_length
                
