#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_lst = []
        total = 0
        seen = {}
        for i in range(len(nums)):
            total += nums[i]
            if (total%k in seen and i-seen[total%k] > 1) or (i > 0 and total%k == 0):
                return True    
            
            prefix_lst.append(total%k)
            
            if total%k not in seen:
                seen[total%k] = i
          
        return False
        
# @lc code=end

