class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float('inf')
        closest_sum = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            
            left = i+1
            right = len(nums)-1
            
            while left < right:
                cur_sum = nums[left]+nums[right]+nums[i]
                
                if abs(cur_sum-target) < min_diff:
                    closest_sum = cur_sum
                    min_diff = abs(cur_sum-target)
                    
                if cur_sum < target:
                    left += 1
                    
                else:
                    right -= 1
                
        return closest_sum
