#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#

# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        max_sum = float('-inf')
        second_sum = float('-inf')
        
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
            
        left = 0
        right = firstLen
        
        while right < len(prefix_sum):
            first_sum = prefix_sum[right]-prefix_sum[left]
            
            l1 = 0
            r1 = l1+secondLen

            while r1 <= left:
                second_sum = max(second_sum,prefix_sum[r1]-prefix_sum[l1])
                l1 += 1 
                r1 += 1
                   
            l2 = right
            r2 = l2+secondLen
            
            while r2 < len(prefix_sum):
                second_sum = max(second_sum,prefix_sum[r2]-prefix_sum[l2])
                l2 += 1
                r2 += 1
                    
            max_sum = max(max_sum,first_sum+second_sum)
            second_sum = float('-inf')
           
            left += 1
            right += 1
                        
        return max_sum
# @lc code=end

