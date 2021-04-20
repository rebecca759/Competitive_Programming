class Solution:
    def minOperations(self, n: int) -> int:
        moves = 0
        num = 0
        
        num = (((n-1)*2)+1)//2
        
        while num > 0:
            moves += num
            num -= 2    
            
        return moves
        
