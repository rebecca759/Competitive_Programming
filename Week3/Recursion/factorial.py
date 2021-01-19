#Iterative
def factorial(n):
    fact = 1
    
    for i in range(n,0,-1):
        fact = fact*i
        
    return fact


#Recursive
def factorial(n):
    if n <= 1:
        return 1
    
    return n*factorial(n-1)
