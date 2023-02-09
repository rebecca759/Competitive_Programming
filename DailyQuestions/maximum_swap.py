class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = num
        num = str(num)

        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                pos_num = int(num[:i]+num[j]+num[i+1:j]+num[i]+num[j+1:])
                max_num = max(max_num,pos_num)


        return max_num