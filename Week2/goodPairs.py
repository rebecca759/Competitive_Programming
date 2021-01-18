class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = {}
        pairs = 0
        
        for num in nums:
            if num in num_count:
                num_count[num] += 1
                
            else:
                num_count[num] = 1
                
        for num in num_count:
            if num_count[num] > 1:
                pair = num_count[num]-1
                pairs += pair
                
                while pair > 1:
                    pair = pair-1
                    pairs += pair
                    
        return pairs
            

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = {}
        pairs = 0
        
        for num in nums:
            if num in num_count:
                pairs += num_count[num]
                num_count[num] += 1
                
            else:
                num_count[num] = 1

        return pairs
            
        
