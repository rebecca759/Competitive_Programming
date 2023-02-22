class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        found = True
        secs = 0
        input_s = s
        s = [s[i] for i in range(len(s))]

        while found:
            # print(s)
            found = False
            temp = {}
            for i in range(1,len(s)):
                if s[i] == '1' and s[i-1] == '0':
                    temp[i-1],temp[i] = '1','0'
                    found = True
                    #print(s)

            secs += found
            for ind in temp:
                s[ind] = temp[ind]
            
        return secs
            