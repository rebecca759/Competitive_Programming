class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right_sum = [0]
        result = []
        
        prefSum = 0
        suffSum = 0
        
        for i in range(len(nums)-1):
            prefSum += nums[i]
            
            left_sum.append(prefSum)
            
        for j in range(len(nums)-1,0,-1):
            suffSum += nums[j]
            
            right_sum.append(suffSum)
            
        right_sum.reverse()
        
        for i in range(len(left_sum)):
            if left_sum[i] == right_sum[i]:
                return i
            
        return -1
