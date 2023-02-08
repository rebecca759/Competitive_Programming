class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = []
        dic = defaultdict(list)
        vis = set()

        for a,b in adjacentPairs:
            dic[a].append(b)
            dic[b].append(a)

        def dfs(num):
            nonlocal res,vis,dic
            
            for adj in dic[num]:
                if adj not in vis:
                    vis.add(adj)
                    res.append(adj)
                    dfs(adj)

        for num in dic:
            if len(dic[num]) == 1:
                res.append(num)
                vis.add(num)
                dfs(num)
                break

        return res