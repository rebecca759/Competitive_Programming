def twoSum(nums, target):
    elements = {}
        
    for i in range(len(nums)):
        if (target - nums[i]) in elements:
            return [i,elements[target-nums[i]]]
        
        elements[nums[i]] = i
            
    return None
                
print(twoSum([2,7,11,15],9))
