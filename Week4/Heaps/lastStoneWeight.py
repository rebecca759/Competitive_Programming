import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #use max-heap since we're asked two largest elements
        heap = []
        
        for stone in stones:
            heapq.heappush(heap,-stone)
            
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            
            if x == y:
                continue
                
            else:
                heapq.heappush(heap,y-x)
             
        if len(heap) == 1:
            return (-heap[0])
        
        else:
            return 0
                
            
