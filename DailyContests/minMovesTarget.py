from collections import deque
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        q.append(((0, 0), (0, 1),0))
        moves = 0
        visited = set()
        visited.add((q[0][0],q[0][1]))
        
        
        while q:
            c1, c2, move = q.popleft()
            
            if self.isTarget(c1,c2,n):
                return move
            
            #check if you can go down
            nr1 = c1[0]+1
            nr2 = c2[0] + 1
            
            nc1 = c1[1]+1
            nc2 = c2[1]+1
            
            if nr1 < len(grid) and nr2 < len(grid): 
                if grid[nr1][c1[1]] == 0 and grid[nr2][c2[1]] == 0 and ((nr1,c1[1]),(nr2,c2[1])) not in visited :
                    q.append(((nr1,c1[1]),(nr2,c2[1]),move+1)) #go down - add to head  and tail coordinate
                    
                    visited.add(((nr1,c1[1]),(nr2,c2[1])))
            
            #check if you can go right
            if nc1 < len(grid) and nc2 < len(grid):
                if grid[c1[0]][nc1] == 0 and grid[c2[0]][nc2] == 0 and ((c1[0],nc1),(c2[0],nc2)) not in visited:
                    q.append(((c1[0],nc1),(c2[0],nc2),move+1)) #go right - add to head & tail coordinate
                    visited.add(((c1[0],nc1),(c2[0],nc2)))
                
                            
            #check if your in a Horizontal pos + check if you can go clockwise
            if self.isHorizontal:
                if nr1 < len(grid) and nc2 < len(grid) and grid[nr1][c1[1]] == 0 and grid[nr1][c1[1]+1] == 0 and (c1,(nr1,c1[1])) not in visited: 
                    q.append((c1,(nr1,c1[1]),move+1))   #go clockwise - add to tail coordinate
                    visited.add((c1,(nr1,c1[1])))
            
            #check if your in a vertical pos + check if you can go anti-clockwise
            if self.isVertical:
                if nc1 < len(grid) and nr1 < len(grid) and grid[c1[0]][nc1] == 0 and grid[nr1][nc1] == 0 and (c1,(c1[0],nc1)) not in visited: 
                    q.append((c1,(c1[0],nc1),move+1))   #go anticlockwise - add to tail coordinate
                    visited.add((c1,(c1[0],nc1)))
        return -1
                    
        
    def isHorizontal(self, c1: tuple, c2: tuple):
        return c1[0] == c2[0]

    def isVertical(self, c1:tuple, c2:tuple):
        return c1[1] == c2[1]
    
    def isTarget(self, c1:tuple, c2:tuple, n):
        istargetC1 = c1[0] == n - 1 and c1[1] == n - 2 
        istargetC2 = c2[0] == n - 1 and c2[1] == n - 1
        
        return istargetC1 and istargetC2
