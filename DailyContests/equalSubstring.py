class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff_lst = []
        cost = 0
        length = 0
        max_length = 0
        index = 0
        
        for i in range(len(s)):
            diff_lst.append(abs(ord(s[i]) - ord(t[i])))
            
        print(diff_lst)

          
        for i in range(len(diff_lst)):
            
            while cost + diff_lst[i] > maxCost:
                if maxCost == 0:
                    return length
                
                cost -= diff_lst[index]
                length -= 1
                index += 1

            cost += diff_lst[i]
            length += 1
            
            print(length,cost)
            
            max_length = max(length, max_length)

            
        return max_length
            
