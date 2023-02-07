class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        diff = len(nums)-k

        while diff > 0:
            heappop(nums)
            diff -= 1

        return heappop(nums)