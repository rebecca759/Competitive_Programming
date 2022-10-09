class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        cur_map = defaultdict(int)
        count,cur_len = 0,0
        res = []
        
        for char in s:
            cur_map[char] += 1
            cur_len += 1
            
            if cur_map[char] == counter[char]:
                count += 1
                
            if count == len(cur_map):
                res.append(cur_len)
                cur_map = defaultdict(int)
                count,cur_len = 0,0
                
        return res