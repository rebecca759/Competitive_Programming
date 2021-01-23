class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        return self.quickSort(nums,0,len(nums)-1)
        
        
    def quickSort(self,arr, start, end):

        if start >= end:
            return arr

        elif (start < end):
            p = self.partition(arr,start,end)
            self.quickSort(arr,start,p - 1)
            self.quickSort(arr, p + 1,end)

        return arr
        

    def partition(self,arr,start,end):
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
