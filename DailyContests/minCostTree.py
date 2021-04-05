class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        res = 0
        
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            
            if min_index == 0:
                res += arr[0]*arr[1]
                
            elif min_index == len(arr)-1:
                res += arr[len(arr)-1]*arr[-2]
                
            else:
                res += arr[min_index] * (min(arr[min_index-1],arr[min_index+1]))
                
            arr.pop(min_index)
                
        return res
                
