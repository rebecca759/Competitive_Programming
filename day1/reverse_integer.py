class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        num = ''
        
        if len(str_num) == 1:
            return x
        
        for i in range(len(str_num)-1,-1,-1):
            if str_num[i] == '-':
                pass
            else:
                num += str_num[i]
            
        if len(num) > 10:
            return 0
        
        if str_num[0] == '-':
            if -int(num) > (-2**31):
                return -int(num)
        else:
            if int(num) < (2**31)-1:
                return int(num)
            
        return 0

