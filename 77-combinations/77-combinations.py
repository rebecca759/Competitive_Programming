class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        def find_combs(ind,cur):
            if len(cur) == k:
                res.append(cur)
                
            for i in range(ind,len(nums)):
                find_combs(i+1,cur+[nums[i]])
                
            
                
        nums = [num for num in range(1,n+1)]
        res = []
        find_combs(0,[])
        return res