class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0 for _ in range(k)]
        logs_dic = defaultdict(set)

        for id,time in logs:
            logs_dic[id].add(time)

        for id in logs_dic:
            res[len(logs_dic[id])-1] += 1

        return res