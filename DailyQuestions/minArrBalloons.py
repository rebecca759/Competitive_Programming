class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        shot = float('-inf')
        ans = 0
        
        print(points)
        
        for p in points:
            if p[0] <= shot <= p[1]:
                continue
                
            else:
                ans += 1
                shot = p[1]
                
        return ans
