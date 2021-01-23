class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        return self.mergeSort(nums,0,len(nums)-1,[])
        
        
    #Merge Sort

    def mergeSort(self,arr,start,end,r):
        if start < end:
            mid = (start + end) // 2
            p1 = self.mergeSort(arr,start,mid,r)
            p2 = self.mergeSort(arr,mid + 1,end,r)

            #merge the two halves

            r = self.mergeLists(p1,r)
            r = self.mergeLists(p2,r)

            return r

        return [arr[start]]

    def mergeLists(self,l1,l2):
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
        

