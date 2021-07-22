import random

def randomize(n):
    array = [i for i in range(1,n+1)]
    print(array)
    
    for pos in range(len(array)-1,1,-1):
        rn = random.randrange(0,pos-1)
        print(rn)
        array[rn], array[pos] = array[pos], array[rn]

    return array

print(randomize(10))


        

             
             
