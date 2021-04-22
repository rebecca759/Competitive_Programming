import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_pr_dif = []
        pr_sum = 0
        avg_ratio_max = 0
        
        for i in range(len(classes)):
            pr = classes[i][0] / classes[i][1]
            pr_diff = (classes[i][0]+1) / (classes[i][1]+1) - pr
            
            max_pr_dif.append((-pr_diff,classes[i][0],classes[i][1]))
         
        heapq.heapify(max_pr_dif)
        
        while extraStudents > 0:
            cur_max = heapq.heappop(max_pr_dif)
            
            new_diff =  (cur_max[1]+2) / (cur_max[2]+2) - (cur_max[1]+1) / (cur_max[2]+1)
            heapq.heappush(max_pr_dif,(-new_diff,cur_max[1]+1,cur_max[2]+1))
            
            extraStudents -= 1
        
        for diff, passed, total in max_pr_dif:
            cur_pr = passed/total
            pr_sum += cur_pr
            
        avg_ratio_max = pr_sum/len(classes)
        
        return avg_ratio_max
