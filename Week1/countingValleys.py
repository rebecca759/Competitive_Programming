#Counting Valleys

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

<<<<<<< HEAD:Week1/countingValleys.py

=======
>>>>>>> 78ee5ff442cb929367d49dd533112532c2c16a46:day1/countingValleys.py
print(countingValleys(8,'UDDDUDUU'))
