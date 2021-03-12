class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        moves = 0
        
        for i in range(len(A)-1):
            if A[i] >= A[i+1]:
                original = A[i+1]
                A[i+1] = A[i] + 1
                diff = A[i+1] - original
                moves += diff
                
        return moves
                
        
