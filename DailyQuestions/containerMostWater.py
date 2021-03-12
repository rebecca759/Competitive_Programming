class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        width = len(height) - 1
        max_area = 0
        
        area = min(height[left],height[right])*width
        max_area = max(area,max_area)
        width -= 1
        
        
        while left < right:
            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
            
            area = min(height[left],height[right]) * width
            max_area = max(area,max_area)
            width -= 1
            
        return max_area
            
            
