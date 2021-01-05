def countingSort(array):
    max_num = array[0]

    for i in range(1,len(array)):
        if array[i] > max_num:
            max_num = array[i]

    counter_array = (max_num+1) * [0]
    
    for i in array:
        counter_array[i] += 1


    for i in range(len(counter_array)):
        if counter_array[i] > 0:
            print(i)


print(countingSort([7,6,5,4,3,2,1]))
