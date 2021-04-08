class Solution:
    def fractionAddition(self, expression: str) -> str:
        op_lst = deque()
        buffer = ''
        
        
        for op in expression:
            if op in '-+':
                if len(op_lst) > 0:
                    op_lst[-1].append(buffer)
                op_lst.append(op)
                buffer = ''
            
            elif op == '/':
                op_lst.append([buffer])
                buffer = ''
                
            else:
                buffer += op
                
                
        op_lst[-1].append(buffer)
      
        while len(op_lst) > 1:
            first = op_lst.popleft()
            sec = op_lst.popleft()
            
            if len(first) == 1 and first == '-':
                op_lst.appendleft(['-'+sec[0],sec[1]])
                
            elif len(sec) == 1:
                third = op_lst.popleft()
                
                result = self.evalFraction(int(first[0]),int(first[1]),int(third[0]),int(third[1]),sec)
                
                op_lst.appendleft([result[0],result[1]])
            
                
        return op_lst[0][0]+'/'+op_lst[0][1]
        
        
    def evalFraction(self,num1,den1,num2,den2,op):
        res_num = 0
        res_den = self.lcm(den1,den2) if den1 != den2 else den1
        
        if op == '+':
            res_num = ((res_den//den1)*(num1)) + ((res_den//den2)*num2)
            
        else:
            res_num = ((res_den//den1)*(num1)) - ((res_den//den2)*num2)
            
        gcd = self.gcd(max(res_num,res_den),min(res_num,res_den))
        
        res_num //= gcd
        res_den //= gcd
        
        return (str(res_num),str(res_den))
        
    def gcd(self,num1,num2):
        if (num2 == 0):
            return num1
        
        return gcd(num2,num1%num2)
    
    def lcm(self,num1,num2):
        gcd = self.gcd(max(num1,num2),min(num1,num2))
        
        return num1*num2// gcd
