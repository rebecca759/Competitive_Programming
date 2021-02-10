import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        result = []
        
        freq_dict = {}
        
        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
                
            else:
                freq_dict[word] = 1
                
        for key in freq_dict:
            heapq.heappush(heap,(-freq_dict[key],key))
            
        while k > 0:
            s = heapq.heappop(heap)
            result.append(s[1])
            k -= 1
            
        return result
            
