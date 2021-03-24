#Bottom-Up Approach
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        ind = 0
        
        for i in range(len(triangle)-1,-1,-1):
            dp.append([0]*len(triangle[i]))
            for j in range(len(triangle[i])):
                if i == len(triangle)-1:
                    dp[ind][j] = (triangle[i][j])
                    
                else:
                    min_val =  min(dp[ind-1][j],dp[ind-1][j+1])
                    
                    dp[ind][j] = triangle[i][j] + min_val       
                    
            ind += 1

        return dp[-1][0]


#Top-down Approach
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        visited = {}
        return self.dfs(visited,triangle,0,0)
        
    def dfs(self,visited,triangle,i,j):
        if (i,j) in visited:
            return visited[(i,j)]
        
        if i == len(triangle)-1:
            visited[(i,j)] = triangle[i][j]
            return triangle[i][j]
        
        new_row = i + 1
        new_col = j 
        new_col2 = j + 1

        v1 = self.dfs(visited,triangle,new_row,new_col)
        v2 = self.dfs(visited,triangle,new_row,new_col2)
            
        val = min(v1,v2) + triangle[i][j]
        visited[(i,j)] = val
        
        return val
