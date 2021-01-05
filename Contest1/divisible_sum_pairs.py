<<<<<<< HEAD
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if ((ar[i]+ar[j]) % k == 0):
                count += 1
                
    return count
=======
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if ((ar[i]+ar[j]) % k == 0):
                count += 1
                
    return count
>>>>>>> 78ee5ff442cb929367d49dd533112532c2c16a46
