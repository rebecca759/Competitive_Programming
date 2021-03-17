class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        max_dist = 0
        
        while left < len(s) and right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                
            else:
                seen.remove(s[left])
                new_dist = right - left
                max_dist = max(new_dist,max_dist)
                left += 1

                
        max_dist = max(right - left,max_dist)
        
        return max_dist
                
