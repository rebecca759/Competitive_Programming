#Merge Sort

def mergeSort(arr,start,end,r):

    if start < end:
        mid = (start + end) // 2
        mergeSort(arr,start,mid,r)
        mergeSort(arr,mid + 1,end,r)

        #merge the two halves?
    print(arr[start])
   
    return arr[start]


arr = [38,27,43,3,9,82,10]

print(mergeSort(arr,0,len(arr)-1,[]))
