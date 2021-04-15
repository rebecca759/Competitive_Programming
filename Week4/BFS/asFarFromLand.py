class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        
        water, land = 0, 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    visited.add((i,j))
                    
                    if land == 0:
                        land += 1
                    
                if water == 0 and grid[i][j] == 0:
                    water += 1
                    
        if water == 0 or land == 0:
            return -1
        
        #BFS
        return self.BFS(grid,visited,queue)
    
    def BFS(self,grid,visited,queue):
        max_dist = 0
        
        while queue:
            row, col, dist = queue.popleft()
            
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for d in directions:
                nr = row + d[0]
                nc = col + d[1]

                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or (nr,nc) in visited:
                    continue

                queue.append((nr,nc,dist+1))
                visited.add((nr,nc))
            
            
            max_dist = max(dist,max_dist)
            
        return max_dist
        
