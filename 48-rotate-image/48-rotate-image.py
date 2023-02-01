class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose matrix
        for i in range(len(matrix)):
            for j in range(i,len(matrix[i])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
          
        #Reverse each row      
        for i in range(len(matrix)):
                l = 0
                r = len(matrix[i])-1
                
                while l < r:
                    matrix[i][l],matrix[i][r] = matrix[i][r],matrix[i][l]
                    l += 1
                    r -= 1

                