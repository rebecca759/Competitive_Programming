def counting_sort2(array):
    max_num = array[0]
    min_num = array[0]

    counter_array = []
    j = 0

    #Find maximum, minimum
    for i in range(1,len(array)):
        if array[i] > max_num:
            max_num = array[i]

        if array[i] < min_num:
            min_num = array[i]

    #Create counter array
    counter_array = (-(min_num)+max_num+1) * [0]

    for num in array:
        counter_array[num+(-min_num)] += 1

    for i in range(len(counter_array)):
        for _ in range(counter_array[i]):
            if counter_array[i] > 0:
                array[j] = i + min_num
                j += 1
            

    return array
            

print(counting_sort2([3,-1,2,-1,2,0,-3]))
print(counting_sort2([7,6,5,4,3,2,1,-1,-2]))
