#Iterative
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        f0 = 0
        f1 = 1
        
        for i in range(2,n+1):
            fib = f0 + f1
            
            f0 = f1
            f1 = fib
                 
        return fib


#Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        return self.fib(n-1)+self.fib(n-2)
