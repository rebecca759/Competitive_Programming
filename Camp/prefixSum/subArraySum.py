class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = {0:1}
        
        totalSum = 0
        count = 0
        
        for num in nums:
            totalSum += num
            
            complement = totalSum - k
            
            if complement in prefix_dict:
                count += prefix_dict[complement]
            
            if totalSum in prefix_dict:
                prefix_dict[totalSum] += 1
                
            else:
                prefix_dict[totalSum] = 1
 
                
        return count
                
