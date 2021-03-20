class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num_province = 0
        n = len(isConnected)
        
        for i in range(len(isConnected)):
            if i not in visited:
                num_province += 1
                self.dfs(i,isConnected,visited)
                
        return num_province
                
    def dfs(self,row,matrix,visited):
        visited.add(row)
        
        for j in range(len(matrix[row])):
            if matrix[row][j] == 1 and j not in visited:
                self.dfs(j,matrix,visited)
                
        return
