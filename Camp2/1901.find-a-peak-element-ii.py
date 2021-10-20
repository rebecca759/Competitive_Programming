#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left = 0
        right = len(mat[0])-1
        
        while left <= right:
            mid = (left+right)//2
            print(mid,left,right)
            
            right_lst = []
            left_lst = []
            
            for i in range(len(mat)):
                top_val = -1 if i == 0 else mat[i-1][mid]
                bot_val = -1 if i == len(mat)-1 else mat[i+1][mid]
                
                left_val = -1 if mid == 0 else mat[i][mid-1]
                right_val = -1 if mid == len(mat[0])-1 else mat[i][mid+1]
                
                val = mat[i][mid]
                
                #check left and right
                if (val > left_val and val > right_val) and (val > top_val and val > bot_val):
                    return [i,mid]

                elif val < left_val:
                    right_lst.append(mid-1)

                elif val < right_val:
                    left_lst.append(mid+1)
                    
            if len(left_lst) > 0:
                left = left_lst[0]
                
            elif len(right_lst) > 0:
                right = right_lst[0]
# @lc code=end

