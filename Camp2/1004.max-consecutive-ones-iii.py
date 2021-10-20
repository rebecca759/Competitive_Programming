#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count = {0:0,1:0}
        max_ones = float('-inf')
        
        while right < len(nums):
                    
            if nums[right] == 0:
                count[0] += 1
                
            else:
                count[1] += 1
                
            while count[0] > k:
                    count[nums[left]] -= 1
                    left += 1
            
            max_ones = max(max_ones,(right-left)+1)
            
            
            right += 1

        return max_ones
        
# @lc code=end

