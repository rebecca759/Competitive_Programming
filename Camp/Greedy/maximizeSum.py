import heapq

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = -A[i]
                K -= 1
                
                if K == 0:
                    break
                
            elif A[i] == 0 or (A[i] > 0 and K % 2 == 0):
                break
                
            else:
                cur_min = min(A)
                j = A.index(cur_min)
                A[j] = -A[j]
                break
            
        return sum(A)
            
                
            
