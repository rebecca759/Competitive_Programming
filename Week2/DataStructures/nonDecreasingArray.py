class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify_count = 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if i == 0 or i+1 == len(nums)-1:
                    nums[i] = nums[i+1]
                    modify_count += 1
                     
                else:
                    if nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i-1]
                        modify_count += 1
                        
                    elif nums[i] <= nums[i+2]:
                        nums[i+1] = nums[i]
                        modify_count += 1
                        
                    else:
                        return False
                    
                    
        return modify_count <= 1
