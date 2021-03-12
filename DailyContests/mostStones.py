class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        matrix = [[0 for i in range(len(stones))] for j in range(len(stones))]
        
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i != j and self.isConnected(stones[i], stones[j]):
                    matrix[i][j] = 1
                    
        print(matrix)
                    
        components = 0
        visited = set()
        
        for i in range(len(matrix)):
            if i not in visited:
                components += 1
                self.dfs(matrix, visited, i)
        return len(stones)-components
    
    def isConnected(self,a: List[int], b: List[int])->bool:
        return a[0] == b[0] or b[1] == a[1]
    
    def dfs(self, matrix: List[List[int]], visited, r):
        if r in visited:
            return
        visited.add(r)
        for j in range(len(matrix)):
            if matrix[r][j] == 1:
                self.dfs(matrix, visited, j)
