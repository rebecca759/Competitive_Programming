class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        s_ind = 0
        
        for i in range(len(t)):
            if t[i] == s[s_ind]:
                s_ind += 1
                if s_ind == len(s):
                    return True
                
        return False
