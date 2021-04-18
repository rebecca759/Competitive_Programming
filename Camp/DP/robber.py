class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        v1 = self.recurse(0,nums,memo)
        v2 = self.recurse(1,nums,memo)
        
        return max(v1,v2)
        
    def recurse(self,index,nums,memo):
        if index >= len(nums):
            return 0
        
        elif index == len(nums)-1:
            return nums[index]
        
        elif index in memo:
            return memo[index]
        
        memo[index] = nums[index] + max(self.recurse(index+2,nums,memo),self.recurse(index+3,nums,memo))
        
        return memo[index]
        
        
    
