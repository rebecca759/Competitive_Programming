from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        found_1 = False
        minutes = 0
        queue = deque()
        index = 0
    
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        #If there are no fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    found_1 = True
                    
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    
        if not found_1:
            return 0
        
        
        #BFS - find number of minutes
        while queue:
            row,col,level = queue.popleft()
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                    continue
                
                if grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col,level+1))
            
            if queue and queue[0][2] > level:
                minutes += 1
                
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1

            
        return minutes
