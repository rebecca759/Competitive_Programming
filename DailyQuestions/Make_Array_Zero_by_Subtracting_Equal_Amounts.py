class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ind = 0
        ops = 0

        while ind < len(nums):
            while nums[ind] <= 0:
                ind += 1
                if ind == len(nums): return ops

            minn = nums[ind]

            for i in range(ind,len(nums)):
                nums[i] -= minn

            ops += 1
            ind += 1

        return ops