class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = self.dfs(visited,grid,0,i,j)
                    
                    max_area = max(area,max_area)
                    
        return max_area
        

    def dfs(self,visited,grid,area,row,col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return area
        
        if grid[row][col] == 0 or (row,col) in visited:
            return area

        visited.add((row,col))
        area += 1

        a1 = self.dfs(visited,grid,area,row+1,col)  
        a2 = self.dfs(visited,grid,0,row,col+1) 
        a3 = self.dfs(visited,grid,0,row-1,col) 
        a4 = self.dfs(visited,grid,0,row,col-1)
        
        return a1 + a2 + a3 + a4
        
