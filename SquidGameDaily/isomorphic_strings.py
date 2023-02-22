class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapa = {}
        mapb = {}
        
        for i in range(len(s)):
            if (s[i] in mapa and t[i] != mapa[s[i]]) or (t[i] in mapb and mapb[t[i]] != s[i]):
                return False
            mapa[s[i]] = t[i]
            mapb[t[i]] = s[i]

        return True