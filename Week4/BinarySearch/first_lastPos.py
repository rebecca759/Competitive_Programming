class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        start = 0
        end = len(nums)-1
        
        def binarySearch(nums,target,start,end):
            if start > end:
                return res
            
            mid = (start + end) // 2
            
            if nums[mid] == target:
                if res[0] == -1:
                    res[0],res[1] = mid,mid
                    
                elif mid < res[0]:
                    res[0] = mid
                    
                elif mid > res[1]:
                    res[1] = mid
                    
                binarySearch(nums,target,start,mid-1)
                binarySearch(nums,target,mid+1,end)
                
            elif nums[mid] < target:
                binarySearch(nums,target,mid+1,end)
                
            elif nums[mid] > target:
                binarySearch(nums,target,start,mid-1)

                
            return res
            
            
        
        return binarySearch(nums,target,start,end)
