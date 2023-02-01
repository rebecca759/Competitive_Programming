class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def generate(cur,op,cl):
            nonlocal res
            if op == 0 and cl == 0:
                res.append(''.join(cur))
                return
            
            if op > 0:
                generate(cur+['('],op-1,cl)
                
            if cl > op:
                generate(cur+[')'],op,cl-1)
                        
        generate([],n,n)
        return res