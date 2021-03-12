class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}
        check_lst = []
        
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
                
            else:
                count_dict[num] = 1
                
        
        for num in count_dict:
            check_lst.append(count_dict[num])
            
        if len(check_lst) == len(set(check_lst)):
            return True
        
        else:
            return False
        
