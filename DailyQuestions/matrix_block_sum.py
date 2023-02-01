class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        res = []
        #Build pref sum matrix
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                prev_row_val = 0 if i-1 < 0 else mat[i-1][j]
                prev_col_val = 0 if j-1 < 0 else mat[i][j-1]
                prev_diag_val = mat[i-1][j-1] if (i-1 >= 0 and j-1 >= 0) else 0

                mat[i][j] += ((prev_row_val+prev_col_val)-prev_diag_val)

        #Calculate result
        for i in range(len(mat)):
            res.append([])
            for j in range(len(mat[i])):
                top_row = max(0,i-k-1)
                bottom_row = min(len(mat)-1,i+k)
                left_col = max(0,j-k-1)
                right_col = min(len(mat[i])-1,j+k)

                total = mat[bottom_row][right_col]
                left_total = mat[bottom_row][left_col] if j-k-1 >= 0 else 0
                top_total = mat[top_row][right_col] if i-k-1 >= 0 else 0
                diag_total = mat[top_row][left_col] if ((i-k-1) >= 0 and (j-k-1) >=0) else 0

                res[-1].append((total-left_total-top_total)+diag_total) 

        return res