class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index_lst = []
        max_dist = 0
        dist = 0
        right_dist = 0
        left_dist = 0
        index = 0
        
        for i in range(len(seats)):
            if seats[i] == 1:
                index_lst.append(i)
                
        left = index_lst[0]
        right = index_lst[0]
        
        if len(index_lst) > 1:
            right = index_lst[1]
            index = 1
        
        for i in range(len(seats)):
            if seats[i] == 1:
                if i == right:
                    left = index_lst[index]
                    index += 1

                    if index < len(index_lst):
                        right = index_lst[index]

                    continue
                    
                else:
                    continue
                
            if i > right:
                if index >= len(index_lst):
                    dist = i - left
                    max_dist = max(max_dist,dist)
                    continue
                    
            if left < i:
                left_dist = i - left
                
            elif left > i:
                dist = left - i
                max_dist = max(max_dist,dist)
                continue
                
            if right > i:
                right_dist = right - i

            dist = min(left_dist,right_dist)
            max_dist = max(max_dist,dist)
         
        return max_dist
