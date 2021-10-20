#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1,1:1}
        self.recurse(n,memo)
        return memo[n]
    
    def recurse(self,n,memo):
        if n in memo:
            return memo[n]
        
        memo[n] = self.recurse(n-1,memo)+self.recurse(n-2,memo)
        return memo[n]
# @lc code=end

