class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = float('-inf')

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_diff = max(max_diff, nums[j]-nums[i])

        return -1 if max_diff == float('-inf') else max_diff