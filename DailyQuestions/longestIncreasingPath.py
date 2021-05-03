class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path = float('-inf')
        memo = {}
        path = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) in memo:
                    path = memo[(i,j)]
                else:
                    path = self.dfs(i,j,memo,matrix,float('-inf'))
                    
                max_path = max(max_path,path)
                    
        return max_path
    
    def dfs(self,i,j,memo,matrix,val):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return 0
        
        elif matrix[i][j] <= val:
            return 0
        
        elif (i,j) in memo:
            return memo[(i,j)]
        
        p1 = 1 + self.dfs(i+1,j,memo,matrix,matrix[i][j])
        p2 = 1 + self.dfs(i,j+1,memo,matrix,matrix[i][j])
        p3 = 1 + self.dfs(i-1,j,memo,matrix,matrix[i][j])
        p4 = 1 + self.dfs(i,j-1,memo,matrix,matrix[i][j])
         
        memo[(i,j)] = max(p1,p2,p3,p4)
        return memo[(i,j)]
