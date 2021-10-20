#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        window_sum = sum(cardPoints[0:(n-k)])
        max_sum = total-window_sum
        print(total,window_sum,max_sum)
        
        left = 0
        right = n-k
        print(left,right)
        
        while right < len(cardPoints):
            window_sum -= cardPoints[left]
            window_sum += cardPoints[right]
            left += 1
            right += 1
            
            max_sum = max(total-window_sum,max_sum)
            print(total,max_sum)
            
        return max_sum
# @lc code=end

