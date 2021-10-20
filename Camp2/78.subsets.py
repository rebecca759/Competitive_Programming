#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        bits = []
        first = 2**(len(nums))
        last = (2**(len(nums))) * 2
        
        for num in range(first,last):
            bits.append(bin(num)[3:])
            
        for item in bits:
            cur = []
            for i in range(len(item)):
                if item[i] == '1':
                    cur.append(nums[i])
                    
            res.append(cur)
            
        return res
        
# @lc code=end

