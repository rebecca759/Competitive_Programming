#Using binary search

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_count = 0
        
        for i in range(len(grid)):
            left = 0
            right = len(grid[i])
            
            while left < right:
                mid = left + (right - left) // 2

                if grid[i][mid] >= 0:
                    left = mid + 1

                else:
                    right = mid
              
            
            neg_count += (len(grid[i]) - left)
            
            
        return neg_count
                
        

#O(n+m) solution - start from bottom of row
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_count = 0
        j_range = len(grid[0])-1
        
        for i in range(len(grid)):
            for j in range(j_range,-1,-1):
                if grid[i][j] >= 0:
                    break
                    
                elif grid[i][j] < 0:
                    neg_count += (len(grid)-i)
                    j_range -= 1
                    
        return neg_count
