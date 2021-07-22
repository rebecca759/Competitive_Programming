class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        print(len(nums))
        nums.sort()
        res = set()
        result = []

        for i in range(2,len(nums)-1):
            for j in range(i+1,len(nums)):
                num = target-(nums[i]+nums[j])
                left = 0
                right = i-1
                
                while left < right:
                    if nums[left]+nums[right] > num:
                        right -= 1
                        
                    elif nums[left]+nums[right] < num:
                        left += 1
                        
                    else:
                        new_res = (nums[i],nums[j],nums[left],nums[right])
                        res.add(new_res)
                        right -= 1 
                        left += 1
             
        for quads in res:
            result.append(list(quads))
            
        return result
