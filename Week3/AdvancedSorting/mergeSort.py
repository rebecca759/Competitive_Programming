#Merge Sort

class mg:
    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.result = []

    
    def mergeSort(self, arr, start, end):
        if start == end:
            return arr[start]
        
        elif start < end:
            mid = (start + end) // 2
            self.p1 = self.mergeSort(arr,start,mid)
            self.p2 = self.mergeSort(arr,mid+1,end)
    
        return self.p1
mer = mg()


arr = [38,27,43,3,9,82,10]
print(mer.mergeSort(arr,0,len(arr)-1))
