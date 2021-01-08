def maximumToys(prices, k):
    amount = 0
    max_items = 0
    j = 0
    
    #sort prices 
    prices.sort()
            
    for num in prices:
        if amount + num > k:
            break
        amount += num
        max_items += 1
        
    return max_items


prices = [1,12,5,111,200,1000,10]
k = 50

print(maximumToys(prices,k))
