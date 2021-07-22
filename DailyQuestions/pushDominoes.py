class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        not_pushed = 0
        res = ''
        
        for i in range(len(dominoes)):
            char = dominoes[i]
            
            if char == '.':
                not_pushed += 1
                
            elif char == 'L':
                if (len(res) == 0 or res[-1] != 'R'):
                    res += 'L'+'L'*(not_pushed)
    
                elif res[-1] == 'R':
                    if not_pushed == 0:
                        res += 'L'
                        
                    else:
                        res += 'R'*(not_pushed//2)
                        
                        if (not_pushed%2 == 1):
                            res += '.'
                        res += 'L'+'L'*(not_pushed//2)
  
                not_pushed = 0
    
            elif char == 'R':
                if res and res[-1] == 'R' and not_pushed > 0:
                    res += 'R'*(not_pushed)
                    
                elif not_pushed > 0:
                    res += '.'*(not_pushed)
                    
                res += 'R'
                not_pushed = 0
        
        if not_pushed > 0 and res and res[-1] == 'R':
            res += 'R'*(not_pushed)
            
        elif not_pushed > 0:
            res += '.'*(not_pushed)
            
        return res
