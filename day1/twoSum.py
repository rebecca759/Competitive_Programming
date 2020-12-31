class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elements = {}
        
        for index,number in enumerate(nums):
            if (target - number) in elements:
                return [index, elements[target-number]]
            
            elements[number] = index
            
        return None
                
