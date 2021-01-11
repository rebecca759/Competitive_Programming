def buildArray(target,n):
    number = 1
    result = []
    
    for i in range(len(target)):
        if target[i] == number:
            result.append('Push')
            
        else:
            while target[i] != number:
                result.append('Push')
                result.append('Pop')
                number += 1
            
            result.append('Push')
                
        number += 1
                
    return result


print(buildArray([2,3,4],4))
