class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        cur_cost = 0
        max_length = 0
        
        left = 0
        right = 0
        
        differences = {}
        
        while left < len(s) and right < len(s):
            diff = abs(ord(s[right]) - ord(t[right]))
            
            if cur_cost + diff > maxCost:
                if left in differences:
                    cur_cost -= differences[left]
                    max_length = max(max_length, right - left)
                    left += 1
                    
                else:
                    left += 1
                    right = left
                

            else:
                cur_cost += diff
                
                if right not in differences:
                    differences[right] = diff
                    
                right += 1
                
                
        max_length = max(max_length, right - left)
        
        return max_length
