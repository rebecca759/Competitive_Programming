class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = [[plantTime[i],growTime[i]] for i in range(len(plantTime))]
        arr.sort(key=lambda x:x[1],reverse=True)
        max_day = float('-inf')
        cur_day = 0

        for plant_time,growtime in arr:
            cur_day += plant_time

            max_day = max(max_day,cur_day+growtime)

        return max_day