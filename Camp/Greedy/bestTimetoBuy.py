class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        left = 0
        right = 1
        profit = 0
        
        while right < len(prices):
            if prices[left] > prices[right]:
                left += 1
                right += 1
                
                
            elif prices[left] <= prices[right]:
                if right == len(prices)-1:
                    profit += (prices[right]-prices[left])
                    return profit
                    
                else:
                    if prices[right] < prices[right+1]:
                        while right < len(prices)-1 and prices[right] <                                       prices[right+1]:
                            right += 1
                            
                        profit += (prices[right]-prices[left])
                        
                        left = right+1
                        right = left + 1
                           
                    else:
                        profit += (prices[right]-prices[left])
                        right += 1
                        left += 1
         
        return profit
