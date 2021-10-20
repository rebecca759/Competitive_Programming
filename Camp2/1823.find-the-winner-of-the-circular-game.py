#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = []
        start = 0
        
        for i in range(n):
            lst.append(i+1)
            
        while len(lst) > 1:
            end = (start+(k-1))%len(lst)
            print(start,end,lst,lst[end])
            lst.pop(end)
            
            start = (end+1)%len(lst)
            
            
        return lst[-1]
# @lc code=end

