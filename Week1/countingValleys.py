def countingValleys(steps, path):
    sea_level = 0
    valley = 0
    i = 0
    
    for i in range(len(path)):
        if path[i] == 'U':
            sea_level += 1

        elif path[i] == 'D':
            sea_level -= 1
            
        if sea_level == 0 and path[i] == 'U':
                valley += 1
               
            
    return valley


print(countingValleys(8,'UDDDUDUU'))
