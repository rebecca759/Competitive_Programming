class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_logs = {}
        res = [0] * k
        
        for pair in logs:
            if pair[0] in user_logs:
                user_logs[pair[0]].add(pair[1])
                
            else:
                s = set()
                s.add(pair[1])
                user_logs[pair[0]] = s
                
        
        for user in user_logs:
            n = len(user_logs[user])
            res[n-1] += 1
            
        return res
