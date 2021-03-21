class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_lst = [1]
        suffix_lst = [1]
        res_lst = []
        
        pref_prod = 1
        suff_prod = 1
        
        for i in range(len(nums)-1):
            pref_prod *= nums[i]
            
            prefix_lst.append(pref_prod)
            
        for j in range(len(nums)-1,0,-1):
            suff_prod *= nums[j]
            
            suffix_lst.append(suff_prod)
            
        suffix_lst.reverse()
        
        for i in range(len(suffix_lst)):
            res_lst.append(suffix_lst[i]*prefix_lst[i])
            
        return res_lst
            
        
