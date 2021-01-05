# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if ((ar[i]+ar[j]) % k == 0):
                count += 1
                
    return count
