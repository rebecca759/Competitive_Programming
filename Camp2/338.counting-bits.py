#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(1,n+1):
            bin_num = bin(i)[2:]
            res.append(bin_num.count('1'))
            
        return res
            
# @lc code=end

