import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1 or n == 0:
            return 0

        #Sieve of Eratosthenes
        
        primes = [True]*n
        
        primes[0] = False
        primes[1] = False
        
        count_primes = 0
        sqroot = int(math.sqrt(n))
        
        for i in range(2,sqroot+1):
            if primes[i]:
                for j in range(i*i,len(primes),i):
                    primes[j] = False         
                
        for val in primes:
            if val:
                count_primes += 1
                
        return count_primes
            
        
