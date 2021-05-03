class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        diffs = []
        
        for i in range(len(nums)-1):
            diffs.append(nums[i]-nums[i+1])
            
        i = 0
        j = 1
        subs = 0
        
        while j < len(diffs):
            if diffs[i] == diffs[j]:
                subs += (j-i)
                j += 1
                
            else:
                i = j
                j += 1
                    
        return subs
