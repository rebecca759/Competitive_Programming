def bubbleSort(array):
    swapped = True
    last_index = len(array)-1

    while swapped:
        swapped = False
        for i in range(last_index):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]
                swapped = True

        last_index -= 1

    return array


print(bubbleSort([7,6,5,4,3,2,1]))
        
