#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        return self.recurse(0,mapping,digits,'',res)
        
    def recurse(self,index,mapping,digits,cur,res):
        if index == len(digits):
            if cur:
                res.append(cur)
            return res
        
        for letter in mapping[digits[index]]:
            cur += letter
            self.recurse(index+1,mapping,digits,cur,res)
            cur = cur[0:len(cur)-1]
                
        return res 
# @lc code=end

