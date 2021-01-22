def quickSort(arr, start, end):
    if start >= end:
        return arr
    
    elif (start < end):
        p = partition(arr,start,end)
        quickSort(arr,start,p - 1)
        quickSort(arr, p + 1,end)

    return arr
        

def partition(arr,start,end):
    pivot_index = start
    store_index = pivot_index + 1
    swap = False
    
    for i in range(pivot_index + 1,end+1):
        if arr[i] < arr[pivot_index]:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
            swap = True

    if swap:
        arr[pivot_index] , arr[store_index - 1] = arr[store_index - 1],arr[pivot_index]
        pivot_index = store_index - 1

    return pivot_index
        

arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

print(quickSort(arr,0,len(arr)-1))
