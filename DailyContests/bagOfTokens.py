class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        max_score = 0
        left = 0
        right = len(tokens)-1
        
        tokens.sort()
        
        while left <= right:
            if P >= tokens[left]:
                P = P - tokens[left]
                score += 1
                left += 1
                
            elif score > 0:
                P += tokens[right]
                score -= 1
                right -= 1
            
            else:
                break
                
            max_score = max(score,max_score)
            
        return max_score
                
            
            
        
        
