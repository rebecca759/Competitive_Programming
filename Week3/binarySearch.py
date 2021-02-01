#Iterative
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        first = 0
        last = len(nums)-1
        
        while first <= last:
            mid_index = (first+last)//2

            if target < nums[mid_index]:
                last = mid_index - 1

            elif target > nums[mid_index]:
                first = mid_index + 1

            else:
                return mid_index
        
        return -1
        
#Recursive
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums,target,0,len(nums)-1)
        
        
    def _search(self,nums,target,first,last):
        if first < 0 or last >= len(nums):
            return -1
            
        if first > last:
            return -1
            
        mid = (first + last) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            return self._search(nums,target,mid+1,last)
        
        elif nums[mid] > target:
            return self._search(nums,target,first,mid-1)
