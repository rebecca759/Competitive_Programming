def selectionSort(array):
    swap = False
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i+1,len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
                swap = True

        if swap:
            array[minIndex], array[i] = array[i], array[minIndex]

        print(array)

    return array


print(selectionSort([9,8,7,6,5,4,3,2,1]))
