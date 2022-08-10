class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        low,high = 0,r*c-1
        
        while low <= high:
            mid = (low+high)//2
            val = matrix[mid//c][mid%c]
            
            if val < target:
                low = mid+1
            elif val > target:
                high = mid-1
            else:
                return True
     
        return False