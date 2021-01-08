def findMedian(arr):
    #implement counting sort
    max_num = arr[0]
    min_num = arr[0]

    counter_array = []
    j = 0
    
    #Find maximum, minimum
    for i in range(1,len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]

        if arr[i] < min_num:
            min_num = arr[i]

    #Create counter array
    counter_array = (-(min_num)+max_num+1) * [0]

    for num in arr:
        counter_array[num+(-min_num)] += 1

    for i in range(len(counter_array)):
        for _ in range(counter_array[i]):
            if counter_array[i] > 0:
                arr[j] = i + min_num
                j += 1
    
    #find median from sorted array
    #find middle element since size of array is odd
    median_index = len(arr) // 2
    median = arr[median_index]
    
    return median
