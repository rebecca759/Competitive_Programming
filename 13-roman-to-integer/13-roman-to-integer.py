class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        
        for i,char in enumerate(s):
            num += mapp[char]
            
            if (char == 'V' or char == 'X') and (i > 0 and s[i-1] == 'I'):
                num -= 2
                
            elif (char == 'L' or char == 'C') and (i > 0 and s[i-1] == 'X'):
                num -= 20
            
            elif (char == 'D' or char == 'M') and (i > 0 and s[i-1] == 'C'):
                num -= 200
                
                
        return num
    
    2100