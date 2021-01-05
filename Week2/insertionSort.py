def insertionSort(array):
    for i in range(1,len(array)):
        x = array[i]
        for j in range(i-1,-1,-1):
            if array[j] > x:
                array[j+1] = array[j]
                array[j] = x

            else:
                break
            
    return array


print(insertionSort([7,6,5,4,3,2,1]))

print(insertionSort([2,1,2]))
