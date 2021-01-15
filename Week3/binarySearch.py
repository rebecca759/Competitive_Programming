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
        
