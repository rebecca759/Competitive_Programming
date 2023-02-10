class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a1,a2 = [],[]

        for num in nums:
            if num < 0:
                a1.append(num**2)
            else:
                a2.append(num**2)

        return self.merge_arrays(a1[::-1],a2)

    def merge_arrays(self,a1,a2):
        i,j = 0,0
        res = []

        while i < len(a1) or j < len(a2):
            v1 = a1[i] if i < len(a1) else float('inf')
            v2 = a2[j] if j < len(a2) else float('inf')
            
            if v1 <= v2:
                res.append(v1)
                i += 1
            else:
                res.append(v2)
                j += 1

        return res
