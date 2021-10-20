#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix_mat = [[0 for j in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        
        res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        #calculate prefix sum
        for i in range(1,len(prefix_mat)):
            for j in range(1,len(prefix_mat[0])):
                prefix_mat[i][j] = (mat[i-1][j-1]+prefix_mat[i-1][j]+prefix_mat[i][j-1])-prefix_mat[i-1][j-1]
                
         
        for i in range(1,len(prefix_mat)):
            for j in range(1,len(prefix_mat[0])):
                total = 0
                right_total = 0
                left_total = 0
                top_left_total = 0
                
                right_col = min(len(prefix_mat[0])-1,j+k) 
                bot_row = min(len(prefix_mat)-1,i+k)  
                top_row = max(0,i-k-1)
                left_col = max(0,j-k-1)

                total = prefix_mat[bot_row][right_col]
                left_total = prefix_mat[bot_row][left_col]
                top_left_total = prefix_mat[top_row][left_col]
                right_total = prefix_mat[top_row][right_col]

                res[i-1][j-1] = (total - right_total - left_total) + top_left_total
                
        return res
# @lc code=end

