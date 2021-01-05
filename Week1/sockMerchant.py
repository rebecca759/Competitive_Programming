# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairCount = 0;
    l = []
    
    for i in range(n):
        if ar[i] in l:
            pairCount += 1
            l.remove(ar[i])
           
        else:
            l.append(ar[i])
        
    return pairCount
