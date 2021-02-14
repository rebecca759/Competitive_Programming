import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_list = []
        index = 0
        
        
        while (index+1 < len(heights) and len(ladder_list) < ladders):
            if heights[index+1] > heights[index]:
                heapq.heappush(ladder_list, (heights[index+1] - heights[index]))
                
            index += 1
        
        
        while index+1 < len(heights):
            dif = heights[index+1] - heights[index]
            if dif > 0:
                if (len(ladder_list) > 0 and dif > ladder_list[0]):
                    elem = heapq.heappop(ladder_list)
                    heapq.heappush(ladder_list,dif)
                    bricks -= elem
                    
                else:
                    bricks -= dif
                    
            if bricks < 0:
                break
                
            index += 1
            
        
        return index
