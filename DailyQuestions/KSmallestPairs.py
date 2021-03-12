class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        count_lst = []
        res_lst = []
        index = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                count_lst.append((nums1[i],nums2[j],nums1[i]+nums2[j]))
    
        
        #sort based on sum
        count_lst.sort(key = lambda x: x[2])
                    
        while index < len(count_lst) and k > 0:
            res_lst.append([count_lst[index][0],count_lst[index][1]])
            index += 1
            k -= 1
            
        
        return res_lst
                    
                    
                    
