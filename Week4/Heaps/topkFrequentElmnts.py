import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        
        #get frequency of each num
        freq_dict = {}
        
        for i in range(len(nums)):
            if nums[i] in freq_dict:
                freq_dict[nums[i]] += 1
                
            else:
                freq_dict[nums[i]] = 1
                
        for key in freq_dict:
            heapq.heappush(heap, (-freq_dict[key],key))
            
        
            
        while k > 0:
            most_freq = heapq.heappop(heap)[1]
            result.append(most_freq)
            k -= 1
            
        return result
