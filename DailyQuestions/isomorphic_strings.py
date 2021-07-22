class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map1 = defaultdict(chr)
        char_map2 = defaultdict(chr)
        
        for i in range(len(s)):
            char_map1[s[i]] = t[i]
            char_map2[t[i]] = s[i]
        
        for i in range(len(s)):
            if char_map1[s[i]] != t[i] or char_map2[t[i]] != s[i]:
                return False
            
        return True
