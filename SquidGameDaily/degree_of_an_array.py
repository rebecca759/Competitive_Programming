class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        start,end = 0,0
        min_len = float('inf')

        if max_freq == 1:
            return 1

        num_indexes = defaultdict(list)

        for i,num in enumerate(nums):
            num_indexes[num].append(i)

        for num in freq:
            s,e = num_indexes[num][0],num_indexes[num][-1]
            if freq[num] == max_freq:
                lenn = (e-s)+1
                min_len = min(min_len,lenn)

        return min_len