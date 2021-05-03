class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabits = 0
        ans_dict  = {}
        
        for ans in answers:
            if ans in ans_dict:
                ans_dict[ans] -= 1
                if ans_dict[ans] == 0:
                    ans_dict.pop(ans)
            
            else:
                rabits += (1+ans)
                if ans != 0:
                    ans_dict[ans] = ans
        
        return rabits
