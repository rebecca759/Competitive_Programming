# Complete the superDigit function below.
def superDigit(n, k):
    if len(n) == 1:
        return n
    
    total = 0
    for num in n:
        total += int(num)
        
    total = total * k
    
    return superDigit(str(total),1)
        
