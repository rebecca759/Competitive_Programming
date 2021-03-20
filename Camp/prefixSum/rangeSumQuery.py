class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefMatrix = []
        
        for row in matrix:
            pref_lst = []
            pref_sum = 0
            
            for elem in row:
                pref_sum += elem
                pref_lst.append(pref_sum)
                
            self.prefMatrix.append(pref_lst)
            
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = 0
        
        for i in range(row1,row2+1):
            row = self.prefMatrix[i]
            
            if col1 == 0:
                diff = row[col2] - 0
            else:
                diff = row[col2] - row[col1-1]
                
            totalSum += diff
            
        return totalSum
        
