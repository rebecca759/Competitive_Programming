def largestPerimeter(A):
    A.sort()
    perimeter = 0
    sides = []
    
    for i in range(len(A)-1,len(A)-4,-1):
        sides.append(A[i])

    j = 4
    
    zero_area = True
    
    while zero_area:
        zero_area = False
        perimeter = sum(sides)
        p = perimeter / 2
        for i in range(len(sides)):
            if p-sides[i] <= 0:
                zero_area = True
                if len(A)-j > -1:
                    sides[i] = A[len(A)-j]
                    j += 1
                else:
                    return 0
            
    
    return perimeter
