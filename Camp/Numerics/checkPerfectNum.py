import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        sqrt = int(math.sqrt(num))
        divisors = [1]
        
        for i in range(2,sqrt+1):
            if (num%i == 0):
                divisors.append(i)
                divisors.append(num//i)
                
        return sum(divisors) == num
