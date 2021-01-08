import random

def countingSort(array):
    if array == []:
        return
    
    max_num = array[0]
    j = 0

    for i in range(1,len(array)):
        if array[i] > max_num:
            max_num = array[i]

    counter_array = (max_num+1) * [0]
    
    for i in array:
        counter_array[i] += 1

    for i in range(len(counter_array)):
        for _ in range(counter_array[i]):
            array[j] = i
            j += 1

    return array

#Array of numbers from 1 to 10000
nums = [i for i in range(1,1000)]

#randomize numbers
def randomize(array):
    for pos in range(len(array)-1,1,-1):
        rn = random.randrange(0,pos-1)
        array[rn], array[pos] = array[pos], array[rn]

randomize(nums)
print(countingSort(nums))
