class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = defaultdict(int)
        count = 0

        for t in time:
            rem = t%60
            count += dic[60-rem]
            if rem == 0:
                count += dic[0]
            dic[rem] += 1

            

        return count