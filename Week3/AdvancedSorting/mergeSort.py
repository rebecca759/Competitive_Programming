#Merge Sort

def mergeSort(arr,start,end,r):
    if start < end:
        mid = (start + end) // 2
        p1 = mergeSort(arr,start,mid,r)
        p2 = mergeSort(arr,mid + 1,end,r)

        #merge the two halves
        left = p1
        right = p2
        
        r = mergeLists([left],r)
        r = mergeLists([right],r)
        
        print(r)

    return arr[start]

def mergeLists(l1,l2):
    i = j = 0

    result = []

    while i < len(l1) or j < len(l2):
        if i == len(l1):
            result += l2[j:]
            break

        if j == len(l2):
            result += l1[i:]
            break
    
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1

        elif l2[j] < l1[i]:
            result.append(l2[j])
            j += 1

    return result

arr = [38,27,43,3,9,82,10]
print(mergeSort(arr,0,len(arr)-1,[]))
