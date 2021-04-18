class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1):
                    if (i,j) not in visited:
                        self.dfs(i,j,visited,board)
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] ='X'
                        
        return board
                    
                    
    def dfs(self,row,col,visited,board):
        visited.add((row,col))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for d in directions:
            nr = row + d[0]
            nc = col + d[1]

            if nr >= len(board) or nc >= len(board[0]) or nr < 0 or nc < 0:
                continue

            if board[nr][nc] == 'O' and (nr,nc) not in visited:
                self.dfs(nr,nc,visited,board)
                    
                    
                
                
                
            
