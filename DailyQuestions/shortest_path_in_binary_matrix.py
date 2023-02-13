class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        visited = {(0,0)}
        q = deque([(0,0,1)])
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[1,-1],[-1,-1]]

        while q:
            row,col,length = q.popleft()

            if row == n-1 and col == n-1:
                return length

            for r,c in dirs:
                nr,nc = row+r, col+c

                if 0 <= nr and nr < n and 0 <= nc and nc < n and (nr,nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr,nc))
                    q.append((nr,nc,length+1))

        return -1 

