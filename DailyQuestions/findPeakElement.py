class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        
        while i <= j:
            mid = i+(j-i)//2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            
            elif (mid > 0 and nums[mid] < nums[mid-1]):
                j = mid-1
                
            else:
                i = mid+1
