class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        res = [[]]
    
        row,col = 0,0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                
                res[-1].append(mat[i][j])
                
                if col == c-1 and row < r-1:
                    row += 1
                    col = 0
                    res.append([])
                    
                else:
                    col += 1
    

        return res
                        
