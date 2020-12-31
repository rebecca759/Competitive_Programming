#Sock Merchant

def sockMerchant(n, ar):
    pairCount = 0;
    l = set()
    
    for i in range(n):
        if ar[i] in l:
            pairCount += 1
            l.remove(ar[i])
           
        else:
            l.add(ar[i])
        
    return pairCount
