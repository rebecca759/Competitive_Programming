import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros_count = 0
        div = 5
        factors = n // div
        add = 0
        
        while factors > 0:
            zeros_count += factors 
            div *= 5
            factors = n // div
            
        return zeros_count
