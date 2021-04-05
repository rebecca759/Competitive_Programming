class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = {}
        num_pair = 0
        
        pair_lst = []
        
        for pair in dominoes:
            item = (pair[0],pair[1])
            item2 = (pair[1],pair[0])
            
            if item2[0] != item2[1] and item2 in pairs:
                num_pair += pairs[item2]
            
            if item in pairs:
                num_pair += pairs[item]
                pairs[item] += 1
                
            else:
                pairs[item] = 1

                
        return num_pair
