def allCellsDistOrder(R,C,r0,c0):
    distances = {}
    result = []
    
    for row in range(R):
        for col in range(C):
            d = abs(row-r0) + abs(col-c0)
            if d not in distances:
                distances[d] = [[row,col]]
            else:
                distances[d].append([row,col])
            
    for num in sorted(distances):
        for rc in distances[num]:
            result.append(rc)
    
     
    return result

print(allCellsDistOrder(2,3,1,2))
