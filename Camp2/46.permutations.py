#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        return self.recurse(res,nums,[],seen)
        
    def recurse(self,res,nums,cur,seen):
        if len(nums) == len(cur):
            res.append(cur[:])
            return res
        
        for num in nums:
            if num not in seen:
                seen.add(num)
                cur.append(num)
                self.recurse(res,nums,cur,seen)
                cur.pop()
                seen.remove(num)
                
        return res
        
# @lc code=end

